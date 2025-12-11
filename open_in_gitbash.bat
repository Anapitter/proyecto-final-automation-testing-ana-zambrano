@echo off
REM Script para abrir Git Bash en el repositorio actual
REM Uso: open_in_gitbash.bat

setlocal enabledelayedexpansion

set "gitBashPath=C:\Program Files\Git\git-bash.exe"

if not exist "%gitBashPath%" (
    echo.
    echo ⚠️ Git Bash no encontrado en: %gitBashPath%
    echo Por favor, instala Git para Windows desde: https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

set "currentDir=%cd%"

echo.
echo 🚀 Abriendo Git Bash en: %currentDir%
echo.

REM Abre Git Bash en el directorio actual
start "" "%gitBashPath%" --cd="%currentDir%"

echo ✅ Git Bash abierto exitosamente!
echo.
pause
