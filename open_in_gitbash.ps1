# Script para abrir Git Bash en el repositorio actual
# Uso: ./open_in_gitbash.ps1

$gitBashPath = "C:\Program Files\Git\git-bash.exe"

if (-Not (Test-Path $gitBashPath)) {
    Write-Host "⚠️ Git Bash no encontrado en: $gitBashPath" -ForegroundColor Yellow
    Write-Host "Por favor, instala Git para Windows desde: https://git-scm.com/download/win" -ForegroundColor Cyan
    exit 1
}

$currentDir = Get-Location

Write-Host "🚀 Abriendo Git Bash en: $currentDir" -ForegroundColor Green

# Abre Git Bash en el directorio actual
Start-Process -FilePath $gitBashPath -WorkingDirectory $currentDir

Write-Host "✅ Git Bash abierto exitosamente!" -ForegroundColor Green
