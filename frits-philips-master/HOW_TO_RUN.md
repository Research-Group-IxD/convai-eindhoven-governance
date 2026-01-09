# 🚀 How to Run This Project - Complete Guide

This guide will walk you through setting up and running the Frits Voice Cloning chatbot project on Windows.

---

## 📋 Project Overview

This project combines:
- **Frits AI Chatbot** - An AI persona of Frits Philips (founder of Philips)
- **Chatterbox TTS** - Text-to-speech voice synthesis engine
- **Web Interface** - Streamlit-based chat application with voice output
- **API Server** - FastAPI server for standalone TTS services

---

## 🔧 Prerequisites

### Required Software
- **Python 3.10** (recommended for best compatibility with Chatterbox)
- **Git** (if cloning the repository)
- **4GB+ RAM** (8GB+ recommended)
- **2GB+ disk space** (for model downloads)

### Optional
- **NVIDIA GPU with CUDA** (for faster processing)
- **Microphone** (for speech-to-text features)

---

## 📥 Installation

### Step 1: Open PowerShell
Navigate to your project directory:
```powershell
cd C:\Users\yvonn\OneDrive\Documenten\FHICT\semester7\voicecloningpackage
```

### Step 2: Create Virtual Environment (Recommended)
```powershell
# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\Activate.ps1
```

> **Note:** If you get an execution policy error, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### Step 3: Install Dependencies
```powershell
pip install -r requirements.txt
```

**⏱️ Expected time:** 5-10 minutes (first time)  
**📦 Downloads:** ~2GB of PyTorch and model files

### Step 4: Verify Installation (Optional)
```powershell
python test_integration.py
```

This will test:
- ✅ All required packages are installed
- ✅ Chatterbox TTS can initialize
- ✅ Audio synthesis works
- ✅ File saving works

---

## 🎯 Running the Project

You have **three options** for running this project:

---

### **Option 1: Frits Web App (Recommended)** ⭐

The interactive web interface with voice chat.

```powershell
streamlit run FRITSPROJECT\frits_app.py
```

**What happens:**
1. Streamlit server starts on `http://localhost:8501`
2. Browser opens automatically
3. You can chat with Frits via text or voice input
4. Frits responds with both text and spoken audio
5. Audio files are saved to `static\outputs\`

**Features:**
- 💬 Text chat interface
- 🎤 Voice input (click microphone icon)
- 🔊 Audio playback of responses
- 💾 Download audio files
- 📊 Conversation history
- ⚙️ Settings panel (temperature, model selection)

**To stop:** Press `Ctrl+C` in the terminal

---

### **Option 2: Frits Command Line**

Terminal-based chat with voice output.

```powershell
python FRITSPROJECT\frits.py
```

**What happens:**
1. Terminal interface starts
2. Type messages to Frits
3. He responds with text (displayed in terminal)
4. Audio files are generated and saved
5. You can play them with your default media player

**To stop:** Type `exit` or press `Ctrl+C`

---

### **Option 3: TTS Server**

Standalone FastAPI server for text-to-speech API.

```powershell
# Using the batch file
run_server.bat

# OR manually with uvicorn
python server.py
```

**What happens:**
1. FastAPI server starts on `http://localhost:8000`
2. Access API docs at `http://localhost:8000/docs`
3. Submit text via API and receive audio files

**API Endpoints:**
- `POST /synthesize` - Generate speech from text
- `POST /synthesize_multilingual` - Multi-language synthesis
- `POST /voice_cloning` - Clone a voice from audio sample
- `GET /` - Serve web interface

**To stop:** Press `Ctrl+C` in the terminal

---

## 🎮 Usage Examples

### Using the Web App

1. Start the app:
   ```powershell
   streamlit run FRITSPROJECT\frits_app.py
   ```

2. In the browser:
   - Type "Hallo Frits!" in the chat box
   - Press Enter
   - Wait for Frits to respond
   - Audio plays automatically
   - Click 🔊 to replay or download

### Using the API

1. Start the server:
   ```powershell
   python server.py
   ```

2. Test with curl:
   ```powershell
   curl -X POST "http://localhost:8000/synthesize" -H "Content-Type: application/json" -d "{\"text\": \"Hallo wereld\"}"
   ```

3. Or use the interactive docs:
   - Open `http://localhost:8000/docs`
   - Try out the endpoints

---

## ⚙️ Configuration

### Frits Configuration

Edit `FRITSPROJECT\frits_config.json`:

```json
{
  "name": "Frits Philips",
  "api_key": "your-portkey-api-key",
  "model_id": "mistral-medium-2505",
  "description": "Personality description...",
  "instructions": {
    ...
  }
}
```

**Key settings:**
- `api_key` - Your Portkey AI API key
- `model_id` - LLM model to use (mistral, claude, etc.)
- `instructions` - Personality and behavior rules

### TTS Settings

In `FRITSPROJECT\tts_handler.py`, you can adjust:

```python
handler = FritsTTSHandler(
    device="auto",        # "auto", "cuda", "cpu", or "mps"
    save_audio=True,      # Save to file?
    output_dir="static/outputs/"
)
```

### Knowledge Base

Add documents to `FRITSPROJECT\kennis\` folder:
- `.html` files (Wikipedia articles)
- `.pdf` files
- `.txt` files

Frits will automatically load and use them for context.

---

## 🐛 Troubleshooting

### "Module not found" errors
```powershell
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### "CUDA out of memory"
```python
# Edit tts_handler.py, change:
handler = FritsTTSHandler(device="cpu")
```

### "No audio playing in browser"
- Check browser console for errors
- Ensure `static\outputs\` folder exists
- Try a different browser (Chrome recommended)
- Check Windows sound settings

### "Streamlit port already in use"
```powershell
# Use a different port
streamlit run FRITSPROJECT\frits_app.py --server.port 8502
```

### "API key not working"
- Verify your Portkey API key in `frits_config.json`
- Check if you have credits remaining
- Test the API key at [portkey.ai](https://portkey.ai)

### "Models downloading too slowly"
- First run downloads ~2GB, this is normal
- Models are cached for future runs
- Check your internet connection
- Models are stored in `~\.cache\huggingface\`

### "Virtual environment not activating"
```powershell
# Run PowerShell as Administrator and enable scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try again
.venv\Scripts\Activate.ps1
```

---

## 📁 Project Structure

```
voicecloningpackage/
│
├── FRITSPROJECT/              # Main Frits application
│   ├── frits_app.py          # Streamlit web interface ⭐
│   ├── frits.py              # CLI version
│   ├── tts_handler.py        # TTS integration module
│   ├── frits_config.json     # Configuration
│   └── kennis/               # Knowledge base documents
│
├── chatterbox-master/         # TTS engine
│   └── src/chatterbox/       # Core TTS modules
│
├── static/                    # Web assets
│   ├── index.html            # Web UI for TTS server
│   └── outputs/              # Generated audio files
│
├── server.py                  # FastAPI TTS server
├── run_server.bat            # Windows batch script
├── requirements.txt          # Python dependencies
├── test_integration.py       # Integration tests
└── Documentation files       # Guides and docs
```

---

## 🎯 Quick Reference

### Start Commands

| Interface | Command | URL |
|-----------|---------|-----|
| **Web App** | `streamlit run FRITSPROJECT\frits_app.py` | http://localhost:8501 |
| **CLI** | `python FRITSPROJECT\frits.py` | N/A |
| **API Server** | `python server.py` | http://localhost:8000 |

### Common Paths

| Description | Path |
|-------------|------|
| **Audio Output** | `static\outputs\` |
| **Configuration** | `FRITSPROJECT\frits_config.json` |
| **Knowledge Base** | `FRITSPROJECT\kennis\` |
| **Virtual Env** | `.venv\` |

### Keyboard Shortcuts

| Action | Key |
|--------|-----|
| Stop server | `Ctrl+C` |
| Clear terminal | `cls` |
| Exit Frits CLI | Type `exit` |

---

## 📚 Additional Documentation

- **QUICKSTART.md** - 3-step quick start guide
- **README.md** - Project overview and features
- **INTEGRATION_GUIDE.md** - Detailed integration documentation
- **ARCHITECTURE.md** - System design and architecture
- **START_HERE.md** - Getting started guide

---

## 🔒 Important Notes

### Security
- Keep your `frits_config.json` secure (contains API keys)
- Don't commit API keys to version control
- Use environment variables for production

### Performance
- First run is slow (model downloads)
- GPU significantly speeds up processing
- Audio generation takes 2-5 seconds per response
- Streamlit caches resources for faster reloads

### Best Practices
- Use virtual environment to avoid dependency conflicts
- Keep Python at 3.10 for best compatibility
- Update requirements regularly: `pip install -r requirements.txt --upgrade`
- Clear audio cache if disk space is low

---

## 💡 Tips & Tricks

### Speed Up Loading
```python
# In tts_handler.py, preload models
handler = FritsTTSHandler()
handler.preload_models()  # Call once at startup
```

### Change Voice
To use a different voice, add voice cloning:
```python
handler.synthesize(
    text="Hello",
    reference_audio_path="path/to/voice.wav"
)
```

### Batch Processing
Process multiple texts:
```python
texts = ["Text 1", "Text 2", "Text 3"]
for text in texts:
    handler.synthesize(text)
```

### Multilingual Support
```python
# Use multilingual model for other languages
from tts_handler import multilingual_synthesize
multilingual_synthesize("Bonjour le monde", language="fr")
```

---

## 🆘 Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Review the error message carefully
3. Check `INTEGRATION_GUIDE.md` for detailed help
4. Verify all dependencies are installed
5. Try restarting with a fresh virtual environment

---

## ✅ Next Steps

After getting it running:

1. ✅ Test basic functionality
2. ✅ Configure Frits personality in `frits_config.json`
3. ✅ Add documents to knowledge base
4. ✅ Experiment with different voices
5. ✅ Try multilingual features
6. ✅ Integrate with your own projects

---

**Happy chatting with Frits! 🎩🎤**
