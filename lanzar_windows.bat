@echo off
TITLE Mi Aplicacion
echo ==========================================
echo      PREPARANDO EL ENTORNO...
echo ==========================================

:: 1. Intentar instalar dependencias (silenciosamente si ya están)
pip install -r requirements.txt >nul 2>&1

:: 2. Ejecutar el código que está en la carpeta src
python src/main.py

:: 3. Si hay error, pausa para poder leerlo
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo HUBO UN ERROR AL EJECUTAR LA APP.
    pause
)