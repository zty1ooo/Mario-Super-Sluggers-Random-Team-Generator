@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
  py "Randomizer.py"
) else (
  echo Python launcher not found. Install Python 3 and enable the "py" launcher.
)

echo.
pause
