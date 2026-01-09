# Frits + Chatterbox Integration Guide

## Overview

You have successfully integrated the **Frits AI chatbot** with **Chatterbox TTS (Text-to-Speech)** for voice synthesis. Now when you have a conversation with Frits, his responses are automatically converted to speech.

## What Changed

### 1. **New Integration Files**
- `FRITSPROJECT/tts_handler.py` - Main TTS integration module that wraps Chatterbox

### 2. **Updated Files**
- `FRITSPROJECT/frits.py` - CLI version now generates voice output
- `FRITSPROJECT/frits_app.py` - Streamlit web app now generates voice output
- `requirements.txt` - Added necessary dependencies

## Features

✅ **Text-to-Speech Synthesis** - Frits' responses are automatically converted to voice  
✅ **Voice Cloning** - Support for reference audio files (optional)  
✅ **Emotion Control** - Adjust emotional expression in the voice  
✅ **Multiple Formats** - Works with both CLI and Streamlit apps  
✅ **Automatic Device Detection** - Works on CPU, CUDA, and MPS (Mac)  

## Installation

### Step 1: Install Dependencies

```bash
# Navigate to the project directory
cd c:\Users\yvonn\OneDrive\Documenten\FHICT\semester7\voicecloningpackage

# Install requirements
pip install -r requirements.txt
```

⚠️ **Note**: This includes PyTorch which can be large. First install might take 5-10 minutes.

### Step 2: Verify Installation

```bash
python -c "from chatterbox.tts import ChatterboxTTS; print('✓ Chatterbox installed successfully')"
```

## Usage

### Web App (Streamlit)

Run the Streamlit app - it now includes voice synthesis:

```bash
streamlit run FRITSPROJECT/frits_app.py
```

**What you'll see:**
- Chat interface as before
- After Frits responds, an audio player appears with his voice
- The audio is automatically saved to `static/outputs/frits_response.wav`

### CLI App

Run the CLI version with voice output:

```bash
python FRITSPROJECT/frits.py
```

**What you'll see:**
- Chat as before
- After Frits responds, it shows "🎤 Frits spreekt nu..." 
- Audio is saved to `static/outputs/frits_response.wav`

## How It Works

### Architecture

```
User Input (text or speech)
    ↓
Frits AI (LLM) generates response
    ↓
TTS Handler (Chatterbox)
    ↓
Audio synthesis
    ↓
Playback / Save to file
```

### TTS Handler Class

The `FritsTTSHandler` class provides:

```python
from FRITSPROJECT.tts_handler import FritsTTSHandler

# Initialize
handler = FritsTTSHandler(device="auto")

# Synthesize text to speech
wav, sr, file_path = handler.synthesize(
    text="Hallo, ik ben Frits!",
    output_path="output.wav"
)

# Optional: use a reference audio for voice cloning
wav, sr, file_path = handler.synthesize(
    text="Hallo!",
    audio_prompt_path="reference_voice.wav",
    exaggeration=0.7  # Control emotional expression
)
```

## Configuration

### Adjust TTS Parameters

Open `frits_app.py` or `frits.py` and find the TTS synthesis call. You can adjust:

```python
streamlit_synthesize(
    st.session_state.tts_handler,
    bot_text,
    exaggeration=0.5,    # Emotional expression (0.0-1.0)
    temperature=0.8,     # Voice variation (lower = more consistent)
    output_path="static/outputs/frits_response.wav"
)
```

### Voice Cloning (Optional)

To use a specific voice:

1. Prepare a reference audio file (WAV format, at least 5 seconds)
2. Modify the synthesis call:

```python
handler.synthesize(
    text=bot_text,
    audio_prompt_path="path/to/your_voice.wav",
    exaggeration=0.6
)
```

### Multilingual (Optional)

To enable multilingual support:

```python
# In frits_app.py initialization
st.session_state.tts_handler = FritsTTSHandler(
    device="auto", 
    use_multilingual=True  # Enable 23-language support
)

# Then in synthesis
handler.synthesize(
    text="Bonjour!",
    language_id="fr"  # French
)
```

## Output Files

Audio files are saved to: `static/outputs/frits_response.wav`

The directory is created automatically if it doesn't exist.

## Troubleshooting

### Issue: "CUDA out of memory"
**Solution:** Edit `tts_handler.py` and change device to CPU:
```python
handler = FritsTTSHandler(device="cpu")
```

### Issue: "ModuleNotFoundError: No module named 'chatterbox'"
**Solution:** Make sure you ran:
```bash
pip install git+https://github.com/ResembleAI/chatterbox.git
```

### Issue: "No audio is playing in Streamlit"
**Solution:** The audio should show in the chat. Make sure:
1. `static/outputs/` folder exists and is writable
2. Your browser allows audio playback
3. Check the browser console for errors

### Issue: TTS initialization fails silently
**Solution:** The app continues without TTS if it fails to load. Check:
```python
# Add debug output in frits_app.py
print(f"TTS Enabled: {st.session_state.get('tts_enabled')}")
print(f"TTS Handler: {st.session_state.get('tts_handler')}")
```

## Advanced: Custom Voice Training

For best results, provide Chatterbox with a reference audio file of the actual Frits (if available):

```python
# Prepare conditionals once
handler.model.prepare_conditionals(
    wav_fpath="frits_voice_reference.wav",
    exaggeration=0.5
)

# Then synthesize with that voice
handler.synthesize(text="My response")
```

## Performance Notes

- **First run**: Model downloads (~2-3 GB) - takes a few minutes
- **Typical synthesis**: 5-10 seconds per response on GPU, 30-60 seconds on CPU
- **Real-time**: Not suitable for ultra-low latency applications
- **Device**: GPU (CUDA/MPS) recommended for speed

## File Structure

```
FRITSPROJECT/
├── frits.py                    (Updated - CLI with TTS)
├── frits_app.py               (Updated - Streamlit with TTS)
├── frits_config.json
├── tts_handler.py             (NEW - TTS integration)
└── kennis/                     (Knowledge documents)

static/
└── outputs/
    └── frits_response.wav     (Generated audio files)
```

## Next Steps

1. ✅ Test the Streamlit app: `streamlit run FRITSPROJECT/frits_app.py`
2. ✅ Test the CLI app: `python FRITSPROJECT/frits.py`
3. 🔊 Ask Frits questions and listen to the responses
4. 🎯 Optional: Provide your own voice reference for voice cloning

## Support

If you encounter issues:
1. Check this README for troubleshooting
2. Look at the error messages in the terminal
3. Make sure all dependencies are installed: `pip install -r requirements.txt`
4. Verify Chatterbox is installed: `pip install git+https://github.com/ResembleAI/chatterbox.git`

---

Enjoy your Frits voice experience! 🎩🎤
