"""
Quick test script to verify Frits + Chatterbox integration
Run this to check if everything is set up correctly
"""

import sys
import os

def test_imports():
    """Test if all required libraries can be imported"""
    print("🔍 Testing imports...\n")
    
    required_modules = [
        ("portkey_ai", "Portkey AI API"),
        ("rich", "Rich console"),
        ("bs4", "BeautifulSoup"),
        ("pypdf", "PDF reader"),
        ("speech_recognition", "Speech recognition"),
        ("streamlit", "Streamlit"),
        ("torch", "PyTorch"),
        ("torchaudio", "Torchaudio"),
        ("librosa", "Librosa"),
        ("safetensors", "SafeTensors"),
        ("huggingface_hub", "Hugging Face Hub"),
    ]
    
    failed = []
    for module, name in required_modules:
        try:
            __import__(module)
            print(f"✓ {name:30} ({module})")
        except ImportError as e:
            print(f"✗ {name:30} ({module})")
            failed.append(module)
    
    if failed:
        print(f"\n❌ Missing modules: {', '.join(failed)}")
        print("\nInstall them with:")
        print(f"  pip install {' '.join(failed)}")
        return False
    
    print("\n✓ All imports successful!")
    return True

def test_chatterbox():
    """Test if Chatterbox TTS is available"""
    print("\n🎤 Testing Chatterbox TTS...\n")
    
    try:
        from chatterbox.tts import ChatterboxTTS
        print("✓ Chatterbox TTS module found")
        
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"✓ Using device: {device}")
        
        print("\n⏳ Loading Chatterbox model (first time might take a few minutes)...")
        model = ChatterboxTTS.from_pretrained(device=device)
        print(f"✓ Model loaded successfully!")
        print(f"✓ Sample rate: {model.sr}Hz")
        
        return True
    except ImportError as e:
        print(f"✗ Chatterbox not installed: {e}")
        print("\nInstall it with:")
        print("  pip install git+https://github.com/ResembleAI/chatterbox.git")
        return False
    except Exception as e:
        print(f"✗ Error loading Chatterbox: {e}")
        return False

def test_tts_handler():
    """Test the custom TTS handler"""
    print("\n🎧 Testing TTS Handler...\n")
    
    try:
        # Check if tts_handler.py exists
        if not os.path.exists("FRITSPROJECT/tts_handler.py"):
            print("✗ tts_handler.py not found in FRITSPROJECT/")
            return False
        
        print("✓ tts_handler.py found")
        
        # Try importing it
        sys.path.insert(0, "FRITSPROJECT")
        from tts_handler import FritsTTSHandler
        print("✓ FritsTTSHandler imported successfully")
        
        print("\n⏳ Initializing TTS Handler...")
        handler = FritsTTSHandler(device="auto", use_multilingual=False)
        print("✓ TTS Handler initialized successfully!")
        
        return True
    except Exception as e:
        print(f"✗ Error with TTS Handler: {e}")
        return False

def test_frits_config():
    """Check if Frits configuration exists"""
    print("\n⚙️  Testing Frits Configuration...\n")
    
    try:
        if not os.path.exists("FRITSPROJECT/frits_config.json"):
            print("✗ frits_config.json not found")
            print("  Create it in FRITSPROJECT/ directory")
            return False
        
        print("✓ frits_config.json found")
        
        import json
        with open("FRITSPROJECT/frits_config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
        
        print(f"✓ Config loaded successfully")
        print(f"  - Name: {config.get('name', 'N/A')}")
        print(f"  - Model: {config.get('model_id', 'N/A')}")
        
        return True
    except Exception as e:
        print(f"✗ Error loading config: {e}")
        return False

def test_synthesis():
    """Test actual speech synthesis"""
    print("\n🎵 Testing Speech Synthesis...\n")
    
    try:
        sys.path.insert(0, "FRITSPROJECT")
        from tts_handler import FritsTTSHandler
        
        print("⏳ Synthesizing test audio (this may take 30-60 seconds)...")
        handler = FritsTTSHandler(device="auto")
        
        # Create output directory
        os.makedirs("static/outputs", exist_ok=True)
        
        test_text = "Hallo."
        wav, sr, path = handler.synthesize(
            test_text,
            output_path="static/outputs/test_synthesis.wav"
        )
        
        print(f"✓ Synthesis successful!")
        print(f"  - Output: {path}")
        print(f"  - Sample rate: {sr}Hz")
        print(f"  - Duration: {wav.shape[-1] / sr:.2f} seconds")
        
        return True
    except Exception as e:
        print(f"✗ Synthesis failed: {e}")
        print("  (This is OK on first run - Chatterbox is downloading models)")
        return False

def main():
    print("=" * 60)
    print("🎩 Frits + Chatterbox Integration Test")
    print("=" * 60)
    
    results = {
        "Imports": test_imports(),
        "Frits Config": test_frits_config(),
        "Chatterbox": test_chatterbox(),
        "TTS Handler": test_tts_handler(),
    }
    
    print("\n" + "=" * 60)
    print("📋 Test Summary")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status:8} {test_name}")
    
    if all(results.values()):
        print("\n✓ All tests passed! Integration is ready.")
        print("\nNext steps:")
        print("  1. Run Streamlit app: streamlit run FRITSPROJECT/frits_app.py")
        print("  2. Or run CLI app: python FRITSPROJECT/frits.py")
        print("\nCheck INTEGRATION_GUIDE.md for detailed instructions.")
    else:
        print("\n❌ Some tests failed. Check the output above for details.")
        print("\nFor help, see INTEGRATION_GUIDE.md")
    
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Test interrupted by user")
        sys.exit(1)
