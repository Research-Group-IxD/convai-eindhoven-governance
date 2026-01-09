#!/bin/bash

# Title: Frits Philips - Voice AI Setup & Launcher (Linux/Mac)

echo "========================================================"
echo "      Frits Philips - Voice AI Setup & Launcher"
echo "========================================================"

# 1. Determine Python command
PYTHON_CMD="python3"
if ! command -v $PYTHON_CMD &> /dev/null; then
    PYTHON_CMD="python"
fi

if ! command -v $PYTHON_CMD &> /dev/null; then
    echo "[ERROR] Python 3 not found. Please install Python 3.10+."
    exit 1
fi

echo "[INFO] Using Python: $($PYTHON_CMD --version)"

# 2. Setup Virtual Environment
echo ""
echo "[1/4] Checking Virtual Environment..."
if [ ! -d ".venv" ]; then
    echo "    Creating virtual environment..."
    $PYTHON_CMD -m venv .venv
else
    echo "    Virtual environment found."
fi

# Activate virtual environment
source .venv/bin/activate

# 3. Update Dependencies
echo ""
echo "[2/4] Updating Core Dependencies..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1

# 4. Install Packages
echo ""
echo "[3/4] Installing/Verifying Packages (This may take a while)..."

# --- SYSTEM DEPENDENCIES (PORTAUDIO) ---
# PyAudio needs the portaudio C library header files to build.
echo "    - Checking system dependencies for Audio..."

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS: Try Homebrew
    if command -v brew &> /dev/null; then
        if ! brew list portaudio &> /dev/null; then
            echo "      [INFO] 'portaudio' not found. Installing via Homebrew..."
            brew install portaudio
        else
            echo "      [OK] 'portaudio' is installed."
        fi
    else
        echo "      [WARN] Homebrew not found. If 'pip install pyaudio' fails, run: brew install portaudio"
    fi

elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux: Check apt/dnf/pacman
    if command -v apt-get &> /dev/null; then
        # Debian/Ubuntu
        if ! dpkg -l | grep -q portaudio19-dev; then
            echo "      [NOTICE] On Debian/Ubuntu, you likely need 'portaudio19-dev'."
            echo "      [CMD] Run this if setup fails: sudo apt-get install portaudio19-dev"
        fi
    elif command -v dnf &> /dev/null; then
        # Fedora
        echo "      [NOTICE] On Fedora, if setup fails run: sudo dnf install portaudio-devel"
    elif command -v pacman &> /dev/null; then
        # Arch
        echo "      [NOTICE] On Arch, if setup fails run: sudo pacman -S portaudio"
    fi
fi
# ---------------------------------------

echo "    - Installing project requirements..."
pip install -r requirements.txt

# GPU Check Logic (Linux only usually)
echo "    - Checking for GPU..."

if command -v nvidia-smi &> /dev/null; then
    echo "      [INFO] NVIDIA GPU detected."
    # Check if torch has CUDA available
    IS_CUDA=$(python -c "import torch; print(torch.cuda.is_available())")
    
    if [ "$IS_CUDA" == "False" ]; then
        echo "      [WARN] Torch is not using CUDA. Reinstalling with CUDA support..."
        pip uninstall -y torch torchaudio torchvision
        pip install torch torchaudio torchvision
    else
        echo "      [INFO] PyTorch is correctly using CUDA."
    fi
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "      [INFO] macOS detected. Using MPS (Metal Performance Shaders) if available."
else
    echo "      [INFO] No NVIDIA GPU detected. Using CPU execution."
fi

# Ensure critical audio packages
echo "    - Verifying Audio Packages..."
pip install chatterbox-tts pyaudio

# 5. Launch
echo ""
echo "[4/4] Launching Frits..."
echo ""
echo "[NOTE] If Streamlit asks for an email, you can leave it blank and press Enter."
echo "========================================================"
echo ""

streamlit run FRITSPROJECT/frits_app.py
