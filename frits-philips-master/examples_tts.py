"""
Example: Using Chatterbox TTS Handler independently

This shows how to use the TTS handler outside of the Frits apps
for custom voice synthesis applications.
"""

import sys
import os
sys.path.insert(0, "FRITSPROJECT")

from tts_handler import FritsTTSHandler
import torch

def example_basic_synthesis():
    """Simple text-to-speech example"""
    print("📝 Example 1: Basic Text-to-Speech\n")
    
    # Initialize handler
    handler = FritsTTSHandler(device="auto")
    
    # Synthesize text
    text = "Hallo, ik ben Frits Philips, een ondernemer uit Eindhoven."
    print(f"Text: {text}\n")
    
    print("⏳ Generating speech...")
    wav, sr, path = handler.synthesize(
        text,
        output_path="static/outputs/example_basic.wav"
    )
    
    print(f"✓ Done! Audio saved to: {path}\n")

def example_with_emotion():
    """Synthesis with emotional expression control"""
    print("😊 Example 2: With Emotion Control\n")
    
    handler = FritsTTSHandler(device="auto")
    
    texts = [
        ("Ik ben blij!", 0.2),      # Low emotion
        ("Ik ben BLIJ!", 0.7),      # High emotion
        ("Ik ben heel blij!", 1.0), # Maximum emotion
    ]
    
    for text, exaggeration in texts:
        print(f"Text: {text}")
        print(f"Exaggeration: {exaggeration}\n")
        
        wav, sr, path = handler.synthesize(
            text,
            exaggeration=exaggeration,
            output_path=f"static/outputs/example_emotion_{int(exaggeration*10)}.wav"
        )
        print(f"✓ Saved to: {path}\n")

def example_voice_cloning():
    """Synthesis using a reference voice"""
    print("🎙️  Example 3: Voice Cloning\n")
    
    # You would need a reference audio file first
    reference_voice = "path/to/your/voice.wav"
    
    if not os.path.exists(reference_voice):
        print(f"⚠️  Reference voice not found: {reference_voice}")
        print("   To use voice cloning, provide a WAV file (5+ seconds)\n")
        return
    
    handler = FritsTTSHandler(device="auto")
    
    text = "Dit is mijn stem!"
    print(f"Text: {text}")
    print(f"Reference: {reference_voice}\n")
    
    wav, sr, path = handler.synthesize(
        text,
        audio_prompt_path=reference_voice,
        exaggeration=0.5,
        output_path="static/outputs/example_cloned.wav"
    )
    
    print(f"✓ Saved to: {path}\n")

def example_batch_synthesis():
    """Generate multiple audio files in batch"""
    print("📦 Example 4: Batch Synthesis\n")
    
    handler = FritsTTSHandler(device="auto")
    
    responses = [
        "Goedemorgen!",
        "Hoe gaat het met je?",
        "Het weer is mooi vandaag.",
        "Tot ziens!",
    ]
    
    os.makedirs("static/outputs/batch", exist_ok=True)
    
    for i, text in enumerate(responses, 1):
        print(f"[{i}/{len(responses)}] {text}")
        
        wav, sr, path = handler.synthesize(
            text,
            output_path=f"static/outputs/batch/response_{i:02d}.wav"
        )
        print(f"         → {path}\n")

def example_multilingual():
    """Synthesis in multiple languages (requires multilingual model)"""
    print("🌍 Example 5: Multilingual Synthesis\n")
    
    try:
        handler = FritsTTSHandler(device="auto", use_multilingual=True)
        
        texts = {
            "en": "Hello, my name is Frits.",
            "nl": "Hallo, mijn naam is Frits.",
            "fr": "Bonjour, je m'appelle Frits.",
            "de": "Hallo, mein Name ist Frits.",
            "es": "Hola, mi nombre es Frits.",
        }
        
        os.makedirs("static/outputs/multilingual", exist_ok=True)
        
        for lang, text in texts.items():
            print(f"[{lang.upper()}] {text}")
            
            wav, sr, path = handler.synthesize(
                text,
                language_id=lang,
                output_path=f"static/outputs/multilingual/{lang}.wav"
            )
            print(f"        → {path}\n")
    
    except Exception as e:
        print(f"⚠️  Multilingual model not available: {e}")
        print("   Make sure to install: pip install git+https://github.com/ResembleAI/chatterbox.git\n")

def example_custom_parameters():
    """Fine-tune synthesis with advanced parameters"""
    print("⚙️  Example 6: Custom Parameters\n")
    
    handler = FritsTTSHandler(device="auto")
    
    text = "Dit is Frits met aangepaste instellingen."
    
    # These parameters affect the synthesis quality and characteristics
    params = {
        "temperature": 0.6,        # Lower = more consistent, higher = more varied
        "repetition_penalty": 1.2, # Prevent repetition
        "min_p": 0.05,            # Minimum probability threshold
        "top_p": 1.0,             # Top-p sampling
    }
    
    print(f"Text: {text}")
    print(f"Parameters: {params}\n")
    
    wav, sr, path = handler.synthesize(
        text,
        output_path="static/outputs/example_custom.wav",
        **params
    )
    
    print(f"✓ Saved to: {path}\n")

def main():
    print("=" * 60)
    print("🎤 Chatterbox TTS Handler Examples")
    print("=" * 60)
    print()
    
    examples = [
        ("Basic Synthesis", example_basic_synthesis),
        ("Emotion Control", example_with_emotion),
        ("Voice Cloning", example_voice_cloning),
        ("Batch Synthesis", example_batch_synthesis),
        ("Multilingual", example_multilingual),
        ("Custom Parameters", example_custom_parameters),
    ]
    
    print("Available examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"  {i}. {name}")
    print()
    
    # Run all examples (or modify to run specific ones)
    try:
        # Run example 1 (uncomment others as needed)
        example_basic_synthesis()
        
        # example_with_emotion()
        # example_voice_cloning()
        # example_batch_synthesis()
        # example_multilingual()
        # example_custom_parameters()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTroubleshooting:")
        print("  1. Make sure dependencies are installed: pip install -r requirements.txt")
        print("  2. Check that static/outputs/ directory is writable")
        print("  3. For first run, Chatterbox needs to download models (~2GB)")

if __name__ == "__main__":
    main()
