@echo off
echo.
echo ========================================
echo Credit Card Fraud Detection - Quick Start
echo ========================================
echo.
echo This script will set up and run the application.
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Installing Python dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [2/3] Checking for trained model...
if not exist "credit_card_model.pkl" (
    echo WARNING: credit_card_model.pkl not found!
    echo Please run CredFrad.ipynb first to generate the model.
    echo.
    pause
)

echo.
echo [3/3] Starting the application...
echo.
echo The app will start on http://localhost:5000
echo Press Ctrl+C to stop the server.
echo.
python app.py

pause
