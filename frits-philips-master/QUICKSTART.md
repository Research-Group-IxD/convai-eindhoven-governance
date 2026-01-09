# 🎩 Frits + Chatterbox - Quick Start

You now have Frits with voice! Here's how to get started:

## 1️⃣ Install Dependencies (5-10 minutes)

```bash
pip install -r requirements.txt
```

This installs everything needed including Chatterbox TTS.

## 2️⃣ Verify Installation (Optional but recommended)

```bash
python test_integration.py
```

This checks if everything is set up correctly.

## 3️⃣ Run Your Choice

### Option A: Web Interface (Recommended for most users)
```bash
streamlit run FRITSPROJECT/frits_app.py
```
- Opens in your browser
- Chat with Frits
- His responses appear as voice + audio player

### Option B: Command Line
```bash
python FRITSPROJECT/frits.py
```
- Terminal-based chat
- His responses appear as voice files

## 📝 What Changed

| File | Change | Why |
|------|--------|-----|
| `tts_handler.py` | NEW | Wraps Chatterbox TTS functionality |
| `frits_app.py` | Updated | Now generates voice output |
| `frits.py` | Updated | Now generates voice output |
| `requirements.txt` | Updated | Added audio libraries |

## 🎤 How It Works

1. **You type/speak** to Frits
2. **Frits responds** with text via LLM
3. **Chatterbox generates speech** from that text
4. **Audio plays** immediately in the web app
5. **File saves** to `static/outputs/frits_response.wav`

## 🔧 Common Issues

**"No audio module named..."** → Run: `pip install -r requirements.txt`

**"CUDA out of memory"** → Change to CPU (slower but works on any machine)

**"Takes too long to start"** → First run downloads ~2GB. Subsequent runs are much faster.

**"No audio playback in Streamlit"** → Check:
- Browser allows audio playback
- `static/outputs/` folder exists
- Check browser console for errors

## 📚 Full Documentation

See `INTEGRATION_GUIDE.md` for:
- Detailed setup instructions
- Configuration options
- Voice cloning guide
- Multilingual support
- Advanced troubleshooting

## ⚡ Quick Test

Want to test just the TTS without the full app?

```python
from FRITSPROJECT.tts_handler import FritsTTSHandler

# Initialize
handler = FritsTTSHandler()

# Generate speech
wav, sr, file_path = handler.synthesize(
    "Hallo, dit is Frits!"
)
```

## 🎯 Next Steps

1. ✅ Install dependencies
2. ✅ Run the app
3. ✅ Chat with Frits
4. ✅ Listen to his voice
5. 🔊 Adjust settings if desired (see INTEGRATION_GUIDE.md)

---

**Questions?** Check `INTEGRATION_GUIDE.md` for detailed help.

Enjoy your voice-enabled Frits! 🎤🎩
