@echo off
rem Installs or updates uv, then installs Python and a .venv on Windows.
rem No admin rights needed.
rem The Python version comes from .python-version next to this file, the
rem packages from pyproject.toml. Run it again to pick up new packages.
rem
rem Usage: install.bat [folder]
rem   Creates folder\.venv. Without a folder: .venv in the current folder,
rem   which is the folder of this file when you double-click it.
setlocal

rem Resolve the target folder before changing directory, so relative paths work.
set "TARGET=%~1"
if not defined TARGET set "TARGET=%CD%"
for %%I in ("%TARGET%") do set "TARGET=%%~fI"
if "%TARGET:~-1%"=="\" set "TARGET=%TARGET:~0,-1%"
set "VENV=%TARGET%\.venv"

cd /d "%~dp0"

set "UV_BIN=%USERPROFILE%\.local\bin"

where uv >nul 2>nul
if not errorlevel 1 goto update_uv

rem The installer updates PATH for new windows only; make uv usable here too.
set "PATH=%UV_BIN%;%PATH%"
if exist "%UV_BIN%\uv.exe" goto update_uv

echo === Installing uv ===
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
if errorlevel 1 goto failed
goto install_python

:update_uv
echo === Checking for uv updates ===
rem Fails if uv came from winget, pip or scoop; then keep the installed version.
uv self update
if errorlevel 1 echo uv was not updated, continuing with the installed version.

:install_python
uv --version
if errorlevel 1 goto failed

echo.
echo === Installing Python ===
uv python install --default
if errorlevel 1 goto failed

echo.
echo === Resolving packages from pyproject.toml ===
rem Errors in pyproject.toml stop here, before the .venv is touched.
uv lock
if errorlevel 1 goto failed

echo.
echo === Creating or updating %VENV% ===
rem Creates the .venv if missing, then installs, updates or removes packages
rem so they match the dependencies in pyproject.toml (pinned in uv.lock).
set "UV_PROJECT_ENVIRONMENT=%VENV%"
uv sync
if not errorlevel 1 goto synced

echo.
echo === Updating failed, removing and recreating %VENV% ===
rem No ( ) blocks here: a folder name with brackets would break them.
if exist "%VENV%\" rmdir /s /q "%VENV%"
if exist "%VENV%" if not exist "%VENV%\" del /f /q "%VENV%"
if not exist "%VENV%" goto recreate
echo Could not remove %VENV%.
echo Close all programs that use it, or remove it yourself, then run this again.
goto failed

:recreate
uv sync
if errorlevel 1 goto failed

:synced
echo.
"%VENV%\Scripts\python.exe" --version
if errorlevel 1 goto failed
echo Done. Open a new command prompt to use uv and python.
pause
exit /b 0

:failed
echo.
echo Installation failed, see the messages above.
pause
exit /b 1
