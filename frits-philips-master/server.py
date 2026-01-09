from pathlib import Path
import uuid
import shutil
import os
import subprocess
import gc
import re
import sys

from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import torchaudio as ta
import torchaudio.functional as taf
import torch

BASE_DIR = Path(__file__).parent

# Try to import chatterbox. If it fails, try to add the local 'chatterbox' folder to sys.path
# This helps if the user copied the repo but didn't install it via pip.
try:
    import chatterbox
except ImportError:
    # Check for chatterbox-master/src (user's current setup)
    local_cb_master = BASE_DIR / "chatterbox-master" / "src"
    local_cb_std = BASE_DIR / "chatterbox"

    if local_cb_master.exists():
        print(
            f"Chatterbox package not found in environment. Attempting to use local folder: {local_cb_master}"
        )
        sys.path.append(str(local_cb_master))
    elif local_cb_std.exists():
        print(
            f"Chatterbox package not found in environment. Attempting to use local folder: {local_cb_std}"
        )
        sys.path.append(str(local_cb_std))

try:
    from chatterbox.tts import ChatterboxTTS
    from chatterbox.mtl_tts import ChatterboxMultilingualTTS
except ImportError as e:
    print("\nCRITICAL ERROR: Could not import 'chatterbox' library.")
    print(f"Details: {e}")
    print("Please ensure the 'chatterbox' folder is copied into this directory.")
    sys.exit(1)

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

# Directories
STATIC_DIR = BASE_DIR / "static"
OUTPUTS_DIR = STATIC_DIR / "outputs"
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

# audio_files folder (user-provided)
AUDIO_FILES_DIR = BASE_DIR / "audio_files"

# Model placeholders - loaded at startup or lazily
model = None
multilingual_model = None
device = None


def load_model_safe(model_cls, device):
    """Helper to load a model, patching torch.load for CPU if needed."""
    if device == "cpu":
        _torch_load_orig = torch.load

        def _torch_load_cpu(f, *a, **k):
            if "map_location" not in k:
                k["map_location"] = torch.device("cpu")
            return _torch_load_orig(f, *a, **k)

        torch.load = _torch_load_cpu
        try:
            return model_cls.from_pretrained(device=device)
        finally:
            torch.load = _torch_load_orig
    else:
        return model_cls.from_pretrained(device=device)


@app.on_event("startup")
def startup_event():
    global model
    # prefer CUDA if available
    global device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Device selected: {device}")
    # Load default model
    model = load_model_safe(ChatterboxTTS, device)


@app.get("/audio_files")
def list_audio_files():
    """Return a simple list of filenames from the `audio_files` folder."""
    files = []
    if AUDIO_FILES_DIR.exists():
        for f in AUDIO_FILES_DIR.iterdir():
            if f.suffix.lower() in (".wav", ".mp3", ".flac") and f.is_file():
                files.append(f.name)
    return {"files": files}


@app.get("/info")
def get_info():
    """Return server status and device info."""
    return {
        "device": device,
        "gpu_available": torch.cuda.is_available(),
        "gpu_name": (
            torch.cuda.get_device_name(0) if torch.cuda.is_available() else None
        ),
    }


@app.post("/synthesize")
async def synthesize(
    text: str = Form(...),
    use_file: str = Form(None),
    audio_prompt: UploadFile = File(None),
    language_id: str = Form(None),
    cfg_weight: Optional[float] = Form(None),
    exaggeration: Optional[float] = Form(None),
):
    """Synthesize `text`. If `audio_prompt` is uploaded it will be used. Otherwise, if `use_file` names
    a file present in the `audio_files` directory, that file will be used as the audio prompt.
    Returns a JSON object with a `url` pointing to the generated WAV under `/static/outputs/`.
    """
    prompt_path = None

    def ensure_wav(path: str) -> str:
        """Ensure `path` points to a WAV file suitable for librosa/torchaudio.
        Uses torchaudio to load, resample, and strictly normalize the audio to prevent artifacts.
        """
        try:
            print(f"Normalizing audio prompt: {path}")
            wav, sr = ta.load(path)

            # Mix to mono if stereo
            if wav.shape[0] > 1:
                wav = wav.mean(dim=0, keepdim=True)

            # 1. High-pass filter to remove low-freq rumble (DC offset/fart noises)
            # 80Hz cutoff is standard for voice
            try:
                wav = taf.highpass_biquad(wav, sr, cutoff_freq=80.0)
            except Exception as e:
                print(f"Warning: Could not apply highpass filter: {e}")

            # 2. Trim Silence (simple energy based)
            # This fixes the "missing first word" if the prompt ends in silence
            # We trim leading/trailing silence where energy is < -60dB
            # (Removed VAD as it was causing issues)
            pass

            # Determine target sample rate
            target_sr = 22050
            if model is not None:
                target_sr = getattr(model, "sr", 22050)
            elif multilingual_model is not None:
                target_sr = getattr(multilingual_model, "sr", 22050)

            # Resample if needed
            if sr != target_sr:
                resampler = ta.transforms.Resample(sr, target_sr)
                wav = resampler(wav)

            # Strict Peak Normalization to 0.7 (Lowered from 0.9)
            # This prevents the "Audio values outside normalized range" error
            peak = torch.abs(wav).max()
            if peak > 0:
                wav = wav / peak * 0.7

            # Hard clamp to ensure no float errors exceed limits
            wav = torch.clamp(wav, -0.95, 0.95)

            out_path = OUTPUTS_DIR / (Path(path).stem + "_norm.wav")
            ta.save(str(out_path), wav, target_sr)
            print(f"Saved normalized prompt to: {out_path}")
            return str(out_path)

        except Exception as e:
            print(f"Error in ensure_wav (fallback to original): {e}")
            return path  # 1) uploaded prompt takes priority

    if audio_prompt is not None:
        safe_name = uuid.uuid4().hex + "_" + os.path.basename(audio_prompt.filename)
        dest = OUTPUTS_DIR / safe_name
        with open(dest, "wb") as f:
            shutil.copyfileobj(audio_prompt.file, f)
        prompt_path = ensure_wav(str(dest))

    # 2) named file from audio_files
    elif use_file:
        candidate = AUDIO_FILES_DIR / use_file
        if candidate.exists() and candidate.is_file():
            prompt_path = ensure_wav(str(candidate))

    # normalize default generation params
    cw = cfg_weight if cfg_weight is not None else 0.5
    ex = exaggeration if exaggeration is not None else 0.5

    # generate audio: if language_id provided and not English, use multilingual model
    global model, multilingual_model

    use_multilingual = language_id and language_id != "en"
    active_model = None

    if use_multilingual:
        # We need multilingual
        if multilingual_model is None:
            # Unload standard if present
            if model is not None:
                print("Unloading standard model to free VRAM...")
                del model
                model = None
                gc.collect()
                if device == "cuda":
                    torch.cuda.empty_cache()

            print("Loading multilingual model...")
            multilingual_model = load_model_safe(ChatterboxMultilingualTTS, device)

        active_model = multilingual_model
    else:
        # We need standard
        if model is None:
            # Unload multilingual if present
            if multilingual_model is not None:
                print("Unloading multilingual model to free VRAM...")
                del multilingual_model
                multilingual_model = None
                gc.collect()
                if device == "cuda":
                    torch.cuda.empty_cache()

            print("Loading standard model...")
            model = load_model_safe(ChatterboxTTS, device)

        active_model = model

    # Prepare generation arguments
    gen_kwargs = {
        "text": text,
        "cfg_weight": cw,
        "exaggeration": ex,
        "temperature": 0.7,
        "top_p": 0.9,
        # "top_k": 50, # Removed as it is not supported by the multilingual model
    }

    if prompt_path:
        gen_kwargs["audio_prompt_path"] = prompt_path

    if use_multilingual:
        gen_kwargs["language_id"] = language_id

    # Sentence splitting for stability
    # Split by . ? ! followed by space or end of string
    # sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    # sentences = [s.strip() for s in sentences if s.strip()]

    # if not sentences:
    #     sentences = [text]
    sentences = [text]

    print(f"Splitting text into {len(sentences)} chunks: {sentences}")

    generated_pieces = []
    sr = getattr(active_model, "sr", 22050)
    silence = torch.zeros(1, int(sr * 0.2))  # 200ms silence

    for i, sent in enumerate(sentences):
        print(f"Generating chunk {i+1}/{len(sentences)}: '{sent}'")
        gen_kwargs["text"] = sent

        # Generate
        wav_chunk = active_model.generate(**gen_kwargs)

        # Ensure 2D (1, samples)
        if wav_chunk.dim() == 1:
            wav_chunk = wav_chunk.unsqueeze(0)

        generated_pieces.append(wav_chunk.cpu())

        # Add silence between sentences (but not after the last one)
        if i < len(sentences) - 1:
            generated_pieces.append(silence)

    if generated_pieces:
        wav = torch.cat(generated_pieces, dim=1)
    else:
        # Fallback
        gen_kwargs["text"] = text
        wav = active_model.generate(**gen_kwargs)

    out_name = f"{uuid.uuid4().hex}.wav"
    out_path = OUTPUTS_DIR / out_name
    ta.save(str(out_path), wav, active_model.sr)

    return {"url": f"/static/outputs/{out_name}"}


# serve static files (index.html + outputs)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
