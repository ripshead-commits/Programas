@echo off
REM ============================================================================
REM  build.bat - Compila la app a un unico archivo PlantillasFURFRG.exe
REM ============================================================================
REM  Requisitos: Python 3.10 o superior en Windows.
REM  Uso: doble clic en este archivo.
REM  Salida: dist\PlantillasFURFRG.exe
REM ============================================================================

cd /d "%~dp0"
set "PYCMD="

echo.
echo === [1/4] Verificando Python ===
echo.

REM -- Intento 1: comando python --
where python >nul 2>&1
if %errorlevel%==0 (
    python --version >nul 2>&1
    if %errorlevel%==0 set "PYCMD=python"
)

REM -- Intento 2: lanzador py (incluido con Python en Windows) --
if not defined PYCMD (
    where py >nul 2>&1
    if %errorlevel%==0 (
        py --version >nul 2>&1
        if %errorlevel%==0 set "PYCMD=py"
    )
)

REM -- Intento 3: python3 --
if not defined PYCMD (
    where python3 >nul 2>&1
    if %errorlevel%==0 (
        python3 --version >nul 2>&1
        if %errorlevel%==0 set "PYCMD=python3"
    )
)

if not defined PYCMD goto :no_python

echo Comando detectado: %PYCMD%
%PYCMD% --version
echo.

echo === [2/4] Creando entorno virtual (.venv) ===
echo.
if not exist ".venv\Scripts\python.exe" (
    %PYCMD% -m venv .venv
    if errorlevel 1 goto :err_venv
)
echo Entorno virtual listo.
echo.

echo === [3/4] Instalando dependencias ===
echo.
call ".venv\Scripts\activate.bat"
if errorlevel 1 goto :err_activate

python -m pip install --upgrade pip
if errorlevel 1 goto :err_pip

python -m pip install -r requirements.txt
if errorlevel 1 goto :err_pip
echo.

echo === [4/4] Compilando .exe con PyInstaller ===
echo.
if exist "build" rmdir /s /q "build"
if exist "dist"  rmdir /s /q "dist"
python -m PyInstaller --noconfirm --clean app.spec
if errorlevel 1 goto :err_build

echo.
echo ===============================================================
echo  LISTO! El ejecutable se encuentra en:
echo      %cd%\dist\PlantillasFURFRG.exe
echo.
echo  Copialo a cualquier PC Windows y ejecutalo con doble clic.
echo  Los datos del historial se guardaran en plantillas_fur_frg.db
echo  junto al .exe.
echo ===============================================================
echo.
pause
exit /b 0


:no_python
echo.
echo -------------------------------------------------------------------
echo  ERROR: No se encontro Python en el PATH del sistema.
echo.
echo  Soluciones:
echo    1. Instala Python desde https://www.python.org/downloads/
echo       En la PRIMERA pantalla del instalador, marca la casilla
echo       "Add python.exe to PATH" y vuelve a ejecutar este script
echo       desde una ventana CMD NUEVA.
echo.
echo    2. O instalalo desde Microsoft Store: busca "Python 3.13".
echo.
echo  Despues de instalar, abre una NUEVA ventana y ejecuta:
echo      python --version
echo  Deberia mostrar algo como: Python 3.13.x
echo -------------------------------------------------------------------
echo.
pause
exit /b 1


:err_venv
echo.
echo ERROR: No se pudo crear el entorno virtual .venv
echo Comando que fallo: %PYCMD% -m venv .venv
echo.
pause
exit /b 1


:err_activate
echo.
echo ERROR: No se pudo activar el entorno virtual.
echo Borra la carpeta .venv y vuelve a ejecutar build.bat
echo.
pause
exit /b 1


:err_pip
echo.
echo ERROR: Fallo la instalacion de dependencias con pip.
echo Revisa tu conexion a internet y vuelve a ejecutar build.bat
echo.
pause
exit /b 1


:err_build
echo.
echo ERROR: Fallo la compilacion con PyInstaller.
echo Revisa los mensajes anteriores para mas detalle.
echo.
pause
exit /b 1
