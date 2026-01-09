"""
TTS Handler for Frits - Integrates Chatterbox TTS for voice synthesis
"""

import torch
import torchaudio as ta
from pathlib import Path

# Patch perth watermarker if not available
try:
    import perth

    if not hasattr(perth, "PerthImplicitWatermarker"):

        class PerthImplicitWatermarker:
            def apply_watermark(self, wav, sample_rate):
                return wav

        perth.PerthImplicitWatermarker = PerthImplicitWatermarker
except:
    pass


class FritsTTSHandler:
    """
    Wrapper around Chatterbox TTS for generating speech from text
    """

    def __init__(self, device="auto", use_multilingual=False):
        """
        Initialize the TTS handler

        Args:
            device: "auto", "cuda", "cpu", or "mps"
            use_multilingual: Use multilingual model if True
        """
        self.device = self._select_device(device)
        self.use_multilingual = use_multilingual
        self.model = None
        self.sr = None
        self._initialize_model()

    def _select_device(self, device):
        """Automatically select the best available device"""
        if device == "auto":
            if torch.cuda.is_available():
                return "cuda"
            elif torch.backends.mps.is_available():
                return "mps"
            else:
                return "cpu"
        return device

    def _initialize_model(self):
        """Load the Chatterbox model"""
        try:
            if self.use_multilingual:
                from chatterbox.mtl_tts import ChatterboxMultilingualTTS as ModelClass

                name = "Multilingual"
            else:
                from chatterbox.tts import ChatterboxTTS as ModelClass

                name = "Standard"

            print(f"Loading Chatterbox {name} TTS on {self.device}...")
            self.model = ModelClass.from_pretrained(device=self.device)
            self.sr = self.model.sr
            print(f"✓ TTS model loaded (SR: {self.sr}Hz)")

        except Exception as e:
            print(f"✗ Failed to load TTS model: {e}")
            print(
                "Ensure chatterbox is installed: pip install git+https://github.com/ResembleAI/chatterbox.git"
            )
            raise

    def synthesize(
        self,
        text,
        output_path=None,
        audio_prompt_path=None,
        exaggeration=0.8,
        temperature=0.8,
        language_id=None,
        **kwargs,
    ):
        if not self.model:
            raise RuntimeError("Model not initialized.")

        try:
            kwargs.setdefault("cfg_weight", 0.43)

            print(f"Generating speech (lang={language_id}, prompt={audio_prompt_path})")

            # Prepare arguments
            gen_args = {
                "text": text,
                "audio_prompt_path": audio_prompt_path,
                "exaggeration": exaggeration,
                "temperature": temperature,
                **kwargs,
            }
            if self.use_multilingual and language_id:
                gen_args["language_id"] = language_id

            wav = self.model.generate(**gen_args)

            # Post-process
            if isinstance(wav, torch.Tensor):
                if wav.dim() == 1:
                    wav = wav.unsqueeze(0)
                wav = wav.to(dtype=torch.float32)

                # Normalize
                peak = torch.abs(wav).max()
                if peak > 0:
                    wav = wav / peak * 0.7
                wav = torch.clamp(wav, -0.95, 0.95)

            # Save if requested
            if output_path:
                output_path = Path(output_path)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                ta.save(str(output_path), wav, self.sr)
                print(f"✓ Audio saved to {output_path}")
                return wav, self.sr, str(output_path)

            return wav, self.sr, None

        except Exception as e:
            print(f"✗ Error generating speech: {e}")
            raise


# Streamlit-specific helper
def streamlit_synthesize(
    handler,
    text,
    output_path="static/outputs/frits_response.wav",
    audio_prompt_path=None,
    language_id=None,
):
    """Synthesize speech for Streamlit with UI feedback"""
    import streamlit as st

    with st.spinner("🎤 Genereer spraak..."):
        wav, sr, path = handler.synthesize(
            text,
            output_path=output_path,
            audio_prompt_path=audio_prompt_path,
            language_id=language_id,
        )

    if path:
        with st.container():
            st.audio(path, format="audio/wav")

    return wav, sr, path
