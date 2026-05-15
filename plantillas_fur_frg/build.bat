@echo off
REM ============================================================================
REM  build.bat - Compila la aplicación a un único archivo PlantillasFURFRG.exe
REM ============================================================================
REM  Requisitos:
REM    - Tener Python 3.10 o superior instalado en Windows (con PATH activado).
REM    - Tener conexión a internet la primera vez (para descargar dependencias).
REM  Uso:
REM    Doble clic sobre este archivo, o ejecútalo desde una cmd:
REM      build.bat
REM  Salida:
REM    dist\PlantillasFURFRG.exe   ← cópialo y úsalo en cualquier PC Windows
REM ============================================================================

setlocal enabledelayedexpansion
cd /d "%~dp0"

echo.
echo === [1/4] Verificando Python ===
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH.
    echo        Descargalo desde https://www.python.org/downloads/  (marca "Add to PATH")
    pause
    exit /b 1
)
python --version

echo.
echo === [2/4] Creando entorno virtual (.venv) si no existe ===
if not exist ".venv\Scripts\python.exe" (
    python -m venv .venv
    if errorlevel 1 (
        echo ERROR: No se pudo crear el entorno virtual.
        pause
        exit /b 1
    )
)

echo.
echo === [3/4] Instalando dependencias ===
call ".venv\Scripts\activate.bat"
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Fallo la instalacion de dependencias.
    pause
    exit /b 1
)

echo.
echo === [4/4] Compilando .exe con PyInstaller ===
if exist "build" rmdir /s /q "build"
if exist "dist"  rmdir /s /q "dist"
pyinstaller --noconfirm --clean app.spec
if errorlevel 1 (
    echo ERROR: Fallo la compilacion con PyInstaller.
    pause
    exit /b 1
)

echo.
echo ===============================================================
echo  LISTO! El ejecutable se encuentra en:
echo      %cd%\dist\PlantillasFURFRG.exe
echo  Puedes copiarlo a cualquier PC Windows y ejecutarlo.
echo  Los datos del historial se guardaran en plantillas_fur_frg.db
echo  junto al .exe (se crea automaticamente la primera vez).
echo ===============================================================
echo.
pause
