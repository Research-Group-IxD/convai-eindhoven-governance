# 🎩 Frits + Chatterbox Integration Architecture

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERACTION                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────┐         ┌──────────────────────┐      │
│  │  Audio Input         │         │  Text Input          │      │
│  │  (Microphone)        │         │  (Keyboard)          │      │
│  └──────────┬───────────┘         └──────────┬───────────┘      │
│             │                                 │                  │
│             └─────────────────┬────────────────┘                │
│                               │                                  │
│                     ┌─────────▼──────────┐                      │
│                     │  Input Processing  │                      │
│                     │  (Speech to Text)  │                      │
│                     └─────────┬──────────┘                      │
│                               │                                  │
└───────────────────────────────┼──────────────────────────────────┘
                                │
┌───────────────────────────────┼──────────────────────────────────┐
│                        FRITS APPLICATION                         │
├───────────────────────────────┼──────────────────────────────────┤
│                               │                                  │
│  ┌────────────────────────────▼─────────────────┐               │
│  │         Message Processing                    │               │
│  │  (Add to chat history, format)               │               │
│  └────────────────────────┬──────────────────────┘               │
│                           │                                      │
│  ┌────────────────────────▼──────────────────────┐               │
│  │      Build System Prompt                       │               │
│  │  (Frits personality + knowledge)              │               │
│  └────────────────────────┬──────────────────────┘               │
│                           │                                      │
│  ┌────────────────────────▼──────────────────────┐               │
│  │      LLM Request (Portkey)                     │               │
│  │  (Generate response text)                      │               │
│  └────────────────────────┬──────────────────────┘               │
│                           │                                      │
│  ┌────────────────────────▼──────────────────────┐               │
│  │      Response Processing                       │               │
│  │  (Clean, validate)                            │               │
│  └────────────────────────┬──────────────────────┘               │
│                           │                                      │
└───────────────────────────┼──────────────────────────────────────┘
                            │
┌───────────────────────────┼──────────────────────────────────────┐
│                    TTS HANDLER (NEW!)                            │
├───────────────────────────┼──────────────────────────────────────┤
│                           │                                      │
│  ┌────────────────────────▼──────────────────────┐               │
│  │   tts_handler.py                               │               │
│  │   ├─ Device Selection (GPU/CPU/MPS)           │               │
│  │   ├─ Model Loading                             │               │
│  │   ├─ Text Preprocessing                        │               │
│  │   └─ Synthesis Parameters                      │               │
│  └────────────────────────┬──────────────────────┘               │
│                           │                                      │
│  ┌────────────────────────▼──────────────────────┐               │
│  │   ChatterboxTTS (from HuggingFace)             │               │
│  │   ├─ T3 (Text-to-Speech tokens)                │               │
│  │   ├─ S3Gen (Token to Audio)                    │               │
│  │   ├─ VoiceEncoder (Voice cloning)              │               │
│  │   └─ Watermarking                              │               │
│  └────────────────────────┬──────────────────────┘               │
│                           │                                      │
│  ┌────────────────────────▼──────────────────────┐               │
│  │   Audio Output Generation                      │               │
│  │   (WAV format, 22050 Hz)                       │               │
│  └────────────────────────┬──────────────────────┘               │
│                           │                                      │
└───────────────────────────┼──────────────────────────────────────┘
                            │
┌───────────────────────────┼──────────────────────────────────────┐
│                      OUTPUT & PLAYBACK                           │
├───────────────────────────┼──────────────────────────────────────┤
│                           │                                      │
│  ┌────────────────────────▼──────────────────────┐               │
│  │   Save to File                                 │               │
│  │   (static/outputs/frits_response.wav)         │               │
│  └────────────────────────┬──────────────────────┘               │
│                           │                                      │
│              ┌────────────┴────────────┐                         │
│              │                         │                         │
│  ┌───────────▼──────────┐   ┌─────────▼────────┐               │
│  │   Streamlit Display  │   │   CLI Display    │               │
│  │   └─ Audio Player    │   │   └─ File path   │               │
│  └──────────────────────┘   └──────────────────┘               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Component Interaction

```
┌──────────────────┐
│  frits_app.py    │  (Streamlit Web Interface)
│  frits.py        │  (CLI Interface)
└────────┬─────────┘
         │ imports & uses
         │
┌────────▼──────────────────┐
│  tts_handler.py           │  (NEW - Main Integration)
│  ├─ FritsTTSHandler       │
│  │  ├─ __init__()         │
│  │  ├─ synthesize()       │
│  │  ├─ synthesize_and_play()
│  │  └─ _try_play_audio()  │
│  └─ Helper functions      │
└────────┬──────────────────┘
         │ imports
         │
┌────────▼──────────────────┐
│  Chatterbox TTS           │  (External library)
│  ├─ ChatterboxTTS         │
│  ├─ T3 (Text → Tokens)    │
│  ├─ S3Gen (Tokens → Audio)│
│  ├─ VoiceEncoder          │
│  └─ EnTokenizer           │
└────────┬──────────────────┘
         │ uses
         │
┌────────▼──────────────────┐
│  PyTorch Models           │  (HuggingFace)
│  ├─ ResembleAI/chatterbox │
│  ├─ ve.safetensors        │
│  ├─ t3_cfg.safetensors    │
│  ├─ s3gen.safetensors     │
│  └─ tokenizer.json        │
└───────────────────────────┘
```

## Data Processing Pipeline

```
User Input (Text)
    │
    ├─────────────────────────────────────────────┐
    │                                             │
    ▼                                             │
System Prompt                                     │
(Frits personality)                              │
    │                                             │
    ├─────────────────────────────────────────────┤
    │                                             │
    ▼                                             │
LLM Request                                      │
(Portkey + Claude/Mistral)                      │
    │                                             │
    ▼                                             │
Generated Text Response                          │
    │                                             │
    ├──────────┬──────────────────────────────┐  │
    │          │                              │  │
    ▼          ▼                              ▼  ▼
Display in  Save to   ────────────────────> Synthesize
Chat       messages                         with TTS
    │                                         │
    │                                         ▼
    │                                    Text Preprocessing
    │                                         │
    │                                         ▼
    │                                    T3: Text → Tokens
    │                                         │
    │                                         ▼
    │                                    S3Gen: Tokens → Audio
    │                                         │
    │                                         ▼
    │                                    WAV Audio File
    │                                         │
    ├─────────────────────────────────────────┘
    │
    ▼
Display to User
(Chat + Audio Player)
```

## File Relationships

```
Root Directory
│
├── requirements.txt (Updated)
│   └─ Contains: torch, torchaudio, chatterbox, etc.
│
├── QUICKSTART.md (NEW)
│   └─ Quick setup guide
│
├── INTEGRATION_GUIDE.md (Updated)
│   └─ Detailed documentation
│
├── INTEGRATION_COMPLETE.md (NEW)
│   └─ Summary of changes
│
├── test_integration.py (NEW)
│   └─ Verification tests
│
├── examples_tts.py (NEW)
│   └─ Usage examples
│
└── FRITSPROJECT/
    │
    ├── frits.py (Updated)
    │   └─ Imports: tts_handler
    │
    ├── frits_app.py (Updated)
    │   └─ Imports: tts_handler
    │
    ├── tts_handler.py (NEW)
    │   ├─ FritsTTSHandler class
    │   ├─ streamlit_synthesize()
    │   └─ Imports: Chatterbox
    │
    ├── frits_config.json (Unchanged)
    │   └─ Frits personality config
    │
    └── kennis/
        └─ Knowledge documents
```

## Sequence Diagram: User Interaction

```
User         App              TTS Handler      Chatterbox       Files
  │            │                  │               │               │
  ├─Message───>│                  │               │               │
  │            ├─Generate Text─>  │               │               │
  │            │  (via LLM)        │               │               │
  │            │<─Response Text─   │               │               │
  │            │                   │               │               │
  │            ├─Synthesize──────>│               │               │
  │            │                   ├─Load Models->│               │
  │            │                   │<─Models──────│               │
  │            │                   │               │               │
  │            │                   ├─Process Text─┤               │
  │            │                   │               │               │
  │            │                   ├─T3: Text→Tokens┤            │
  │            │                   │               │               │
  │            │                   ├─S3Gen: Tokens→Audio┤        │
  │            │                   │               │               │
  │            │                   ├─Save Audio───────────────>│
  │            │<─Return WAV─      │               │               │
  │            │                   │               │               │
  ├─Display───<│                   │               │               │
  │  (Chat +   │                   │               │               │
  │   Audio)   │                   │               │               │
  │            │                   │               │               │
  │  (Listen)  │                   │               │               │
  │            │                   │               │               │
```

## Integration Points

### Before Integration
```
User ──> Frits App ──> LLM ──> Text Response ──> Display
```

### After Integration
```
User ──> Frits App ──> LLM ──> Text Response ──> [TTS Handler]
                                                     │
                                            ┌────────┴────────┐
                                            │                 │
                                        Chatterbox        Save & Play
                                            │
                                        Voice Output
```

---

## Key Technologies

| Component | Technology | Purpose |
|-----------|-----------|---------|
| LLM | Portkey + Mistral | Generate response text |
| TTS | Chatterbox (ResembleAI) | Convert text to speech |
| Deep Learning | PyTorch | Model inference |
| Audio Processing | Torchaudio, Librosa | Audio handling |
| Web Framework | Streamlit | User interface |
| CLI Framework | Rich | Terminal interface |
| Configuration | JSON | Frits settings |

---

This integration brings together:
- **LLM Responses** (Frits thinking)
- **Voice Synthesis** (Frits speaking)
- **Web Interface** (Streamlit) or **CLI** (Rich)

Creating a complete conversational AI with voice! 🎤🎩
