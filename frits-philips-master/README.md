# Voice Cloning Package - Frits + Chatterbox Integration 🎤🎩

Welcome! This project combines the **Frits AI chatbot** with **Chatterbox text-to-speech** for a complete voice-enabled conversational AI.

## 📋 What's Included

This monorepo contains:

1. **FRITSPROJECT/** - Frits AI with integrated TTS
   - `frits.py` - CLI version with voice output
   - `frits_app.py` - Streamlit web app with voice output  
   - `tts_handler.py` - TTS integration module (NEW)
   - `frits_config.json` - Personality configuration

2. **chatterbox-master/** - TTS engine
   - Text-to-speech synthesis
   - Voice cloning support
   - Multilingual capabilities

3. **Documentation** (NEW)
   - `QUICKSTART.md` - Get started in 3 steps
   - `INTEGRATION_GUIDE.md` - Detailed setup & configuration
   - `ARCHITECTURE.md` - System design & data flow
   - `INTEGRATION_COMPLETE.md` - Changes summary

4. **Testing & Examples** (NEW)
   - `test_integration.py` - Verify installation
   - `examples_tts.py` - Usage examples

## 🚀 Quick Start (3 Steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```
_Takes 5-10 minutes for first install (downloads PyTorch + models)_

### 2. Verify Setup (Optional)
```bash
python test_integration.py
```

### 3. Run the App
```bash
# Web interface (recommended)
streamlit run FRITSPROJECT/frits_app.py

# OR Command line
python FRITSPROJECT/frits.py
```

## ✨ What's New (Integration Complete!)

| Component | Status | What It Does |
|-----------|--------|-------------|
| **TTS Handler** | ✅ NEW | Wraps Chatterbox for easy integration |
| **Voice Output** | ✅ NEW | Frits responses are now spoken |
| **Audio Playback** | ✅ NEW | Streamlit audio player + file save |
| **Device Auto-Detection** | ✅ NEW | GPU/CPU/MPS automatic selection |
| **Documentation** | ✅ NEW | 4 comprehensive guides + examples |

## 📚 Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| `QUICKSTART.md` | Get running fast | Everyone (start here!) |
| `INTEGRATION_GUIDE.md` | Complete setup guide | Users needing configuration |
| `ARCHITECTURE.md` | System design | Developers |
| `INTEGRATION_COMPLETE.md` | What changed | Project managers |

## 🎯 How It Works

```
You: "Hallo Frits!"
        ↓
    Frits AI (LLM)
        ↓
Response: "Hallo! Hoe gaat het?"
        ↓
    Chatterbox TTS
        ↓
🔊 "Hallo! Hoe gaat het?" (spoken)
```

## 💡 Key Features

✅ **Text-to-Speech** - Automatic voice synthesis  
✅ **Voice Cloning** - Use your own voice (optional)  
✅ **Emotion Control** - Adjust expressiveness  
✅ **GPU Support** - Fast inference on CUDA/MPS  
✅ **Web & CLI** - Two interfaces included  
✅ **Multilingual** - 23 languages supported (optional)  
✅ **File Export** - Save audio files  

## 🔧 Technical Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Interface** | Streamlit / Rich | User interaction |
| **LLM** | Portkey + Mistral/Claude | Text generation |
| **TTS** | Chatterbox (ResembleAI) | Speech synthesis |
| **ML Framework** | PyTorch | Model inference |
| **Audio** | Torchaudio, Librosa | Audio processing |

## 📁 Project Structure

```
.
├── FRITSPROJECT/
│   ├── frits.py                (Updated - with TTS)
│   ├── frits_app.py           (Updated - with TTS)
│   ├── tts_handler.py         (NEW - Main integration)
│   ├── frits_config.json      (Configuration)
│   └── kennis/                (Knowledge documents)
│
├── chatterbox-master/         (TTS engine)
│   └── src/chatterbox/        (Models & code)
│
├── static/
│   └── outputs/               (Generated audio files)
│
├── Documentation/
│   ├── QUICKSTART.md          (Start here!)
│   ├── INTEGRATION_GUIDE.md   (Detailed setup)
│   ├── ARCHITECTURE.md        (System design)
│   └── INTEGRATION_COMPLETE.md (Changes)
│
├── test_integration.py        (Verification tests)
├── examples_tts.py            (Usage examples)
├── requirements.txt           (Dependencies)
└── README.md                  (This file)
```

## ⚙️ Installation Details

### Requirements
- Python 3.8+
- 4GB+ RAM
- GPU recommended (optional)

### Install Steps

1. **Clone/Extract** the project
2. **Navigate** to project directory
3. **Install**: `pip install -r requirements.txt`
4. **Run**: `streamlit run FRITSPROJECT/frits_app.py`

## 🧪 Testing

### Quick Test
```python
from FRITSPROJECT.tts_handler import FritsTTSHandler
handler = FritsTTSHandler()
wav, sr, path = handler.synthesize("Hallo!")
```

### Full Verification
```bash
python test_integration.py
```

### Run the Apps
```bash
# Web App
streamlit run FRITSPROJECT/frits_app.py

# CLI App  
python FRITSPROJECT/frits.py
```

## 🎨 Customization

### Adjust Voice Parameters
Edit `frits_app.py` or `frits.py` to change:
- **Emotion** (exaggeration: 0.0-1.0)
- **Voice variation** (temperature: 0.0-1.0)
- **Output location** (path configuration)

### Use Custom Voice
Provide your own reference audio:
```python
handler.synthesize(
    "Your text here",
    audio_prompt_path="your_voice.wav",
    exaggeration=0.6
)
```

### Enable Multilingual
```python
handler = FritsTTSHandler(
    device="auto",
    use_multilingual=True
)
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "No module named..." | Run: `pip install -r requirements.txt` |
| "CUDA out of memory" | Use CPU: Change device to "cpu" |
| No audio playback | Check browser permissions & `static/outputs/` folder |
| Slow startup | First run downloads models (~2GB). Next runs are faster. |

See `INTEGRATION_GUIDE.md` for more troubleshooting.

## 📖 Next Steps

1. **Read**: Start with `QUICKSTART.md`
2. **Install**: Follow installation steps above
3. **Test**: Run `python test_integration.py`
4. **Use**: Run the app and chat!
5. **Customize**: See `examples_tts.py` for advanced usage

## 🤝 Credits

- **Frits Project**: Local chatbot with knowledge base
- **Chatterbox**: [ResembleAI/chatterbox](https://github.com/ResembleAI/chatterbox) TTS engine
- **Portkey**: LLM routing and fallback
- **Streamlit**: Web framework

## 📄 License

See individual component licenses:
- Chatterbox: Check repository
- Streamlit: Apache 2.0
- PyTorch: BSD

## 🆘 Support

- **Setup Issues**: See `QUICKSTART.md`
- **Configuration**: See `INTEGRATION_GUIDE.md`
- **Technical Details**: See `ARCHITECTURE.md`
- **Examples**: See `examples_tts.py`
- **Testing**: Run `test_integration.py`

---

## Summary

✅ **Frits now speaks!** Your AI chatbot is integrated with professional text-to-speech.

Start with `QUICKSTART.md` for the fastest path to a working system.

Enjoy! 🎤🎩

