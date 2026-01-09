import sys
from pathlib import Path
import os

# Add chatterbox to path (simulating what tts_handler does)
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
chatterbox_path = project_root / "chatterbox-master" / "src"
if str(chatterbox_path) not in sys.path:
    sys.path.append(str(chatterbox_path))

try:
    import chatterbox

    print("Successfully imported chatterbox")
    from chatterbox.tts import ChatterboxTTS

    print("Successfully imported ChatterboxTTS")
except ImportError as e:
    print(f"Failed to import: {e}")
    sys.exit(1)
