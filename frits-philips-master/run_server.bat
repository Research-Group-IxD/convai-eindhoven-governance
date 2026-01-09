@echo off
setlocal enabledelayedexpansion
title Frits Philips - Chatterbox Server

echo ========================================================
echo      Frits Philips - Voice AI Setup & Launcher
echo ========================================================

set "PYTHON_CMD="

REM 1. Try finding Python 3.10 via the Windows Launcher (py.exe)
py -3.10 --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_CMD=py -3.10"
    echo [INFO] Found Python 3.10 via Windows Launcher.
    goto :found_python
)

REM 2. Try finding 'python' and check if it is 3.10
python --version 2>&1 | findstr " 3.10" >nul
if %errorlevel% equ 0 (
    set "PYTHON_CMD=python"
    echo [INFO] Default 'python' is 3.10.
    goto :found_python
)

REM 3. Fallback: Use default python but warn
python --version >nul 2>&1
if %errorlevel% equ 0 (
    set "PYTHON_CMD=python"
    echo [WARNING] Specific Python 3.10 not found. Using default:
    python --version
    echo Note: Chatterbox works best with Python 3.10.
    goto :found_python
)

echo [ERROR] Python not found. Please install Python 3.10.
pause
exit /b

:found_python
echo.
echo [1/4] Checking Virtual Environment...
if not exist ".venv" (
    echo     Creating virtual environment...
    %PYTHON_CMD% -m venv .venv
) else (
    echo     Virtual environment found.
)

REM Activate virtual environment
call .venv\Scripts\activate

echo.
echo [2/4] Updating Core Dependencies...
python -m pip install --upgrade pip setuptools wheel >nul 2>&1

echo.
echo [3/4] Installing/Verifying Packages (This may take a while)...

REM 1. Install standard requirements first
echo     - Installing project requirements...
pip install -r requirements.txt

REM 2. Check for GPU and upgrade to CUDA Torch if available
echo     - Checking for NVIDIA GPU...
where nvidia-smi >nul 2>&1
if %errorlevel% equ 0 (
    echo       [INFO] NVIDIA GPU detected. Verifying PyTorch CUDA support...
    python -c "import torch; exit(0 if torch.cuda.is_available() else 1)" >nul 2>&1
    if !errorlevel! neq 0 (
        echo       [WARN] Torch is not using CUDA. Reinstalling with CUDA 12.4 support...
        pip uninstall -y torch torchaudio torchvision
        pip install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cu124
    ) else (
        echo       [INFO] PyTorch is correctly using CUDA.
    )
) else (
    echo       [INFO] No NVIDIA GPU detected. Using CPU execution.
)

REM 3. Explicitly verify critical audio packages
echo     - Verifying Audio Packages...
pip install chatterbox-tts pyaudio

echo.
echo [4/4] Launching Frits...
echo.
echo [NOTE] If Streamlit asks for an email, you can leave it blank and press Enter.
echo.
echo ========================================================
echo.
streamlit run FRITSPROJECT/frits_app.py

pause
