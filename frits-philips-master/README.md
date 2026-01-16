# Voice Cloning Package - Frits + Chatterbox Integration 🎤🎩

Welcome! This project combines the **Frits AI chatbot** with **Chatterbox text-to-speech** for a complete voice-enabled conversational AI.

## 📋 Overview

This project leads the "ConvAI Eindhoven Governance" assignment, creating a digital twin of Frits Philips to interact with citizens about Eindhoven's future and history. It integrates:

- **Frits AI**: Keeps the warm, down-to-earth personality of Frits Philips using an LLM.
- **Chatterbox TTS**: Provides voice synthesis to make Frits actually speak.
- **Multilingual Support**: Switch seamlessly between Dutch and English interactions.

## ⚠️ Important Installation Info

**API INFORMATION**: To procure a chat.fontysict.nl API key, you will have to request one from the ISSD Support Desk. More information can be found here: https://fhict.instructure.com/courses/14338/pages/getting-started-and-access-guide?module_item_id=1321436

**Heavy Download Warning**: The installation process involves downloading **PyTorch** and related audio libraries, which totals approximately **~2GB of data**.

- Python < 3.10 required for Chatterbox-tts usage, anything above 3.10 won't work.
- Portkey API key
- ~4GB ram, ~2GB disk space download, fast GPU for faster audio generation
- Ensure a stable internet connection.
- Allow 5-15 minutes for the initial install.

## 🚀 Quick Start

### Option 1: Easy Install ⚡

**Windows:**

1. Double-click **`run_server.bat`**

**Mac / Linux:**

1. Open terminal
2. Run: `bash run_server.sh`

Wait for the setup to complete (it will install everything for you). The application will launch automatically in your browser.

_Note: These scripts automatically handle Python detection, virtual environment creation, and the ~2GB dependency download._

### Option 2: Manual Setup (3 Steps)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

_Note: This step downloads the ~2GB dependencies._

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

## 4. After installation

Make sure to put the API key for chat.fontysict.nl in the frits_config.json, located under frits-philips-master/FRITSPROJECT/

## 🏗️ Architecture

```
┌─────────────────┐       ┌──────────────┐       ┌─────────────────┐
│   User Input    │  ──►  │   Frits AI   │  ──►  │  Text Response  │
└─────────────────┘       └──────────────┘       └────────┬────────┘
                                                         │
┌─────────────────┐       ┌──────────────┐               │
│  Audio Output   │  ◄──  │  TTS Engine  │  ◄────────────┘
└─────────────────┘       └──────────────┘
```

## 📂 Key Files & Structure

- **`FRITSPROJECT/`**: Main application code.
  - `frits_app.py`: Streamlit interface.
  - `tts_handler.py`: TTS wrapper.
  - `frits_config.json`: Persona settings.
- **`chatterbox-master/`**: Local TTS engine source.
- **`server.py`**: Standalone TTS API server.
- **`Documentation/`**: Detailed guides (`QUICKSTART.md`, `INTEGRATION_GUIDE.md`, etc.).

## 🔧 Troubleshooting

- **Slow First Run?** Normal behaviour; it's downloading the model weights.
- **No Sound?** Check your browser permissions for auto-play audio.
- **Import Errors?** Ensure `chatterbox-master` is in the root directory.

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

---

## Summary

✅ **Frits now speaks!** Your AI chatbot is integrated with professional text-to-speech.

Start with `QUICKSTART.md` for the fastest path to a working system.

Enjoy! 🎤🎩
