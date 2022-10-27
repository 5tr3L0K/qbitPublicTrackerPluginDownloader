Write-Host -ForegroundColor DarkGreen "INSTALANDO PYENV..."
choco install pyenv-win -y | Out-Null
Write-Host -ForegroundColor DarkGreen "INSTALANDO PYTHON 3.10.8..."
pyenv install 3.10.8 | Out-Null
Write-Host -ForegroundColor DarkGreen "ACTIVANDO PYTHON..."
pyenv shell 3.10.8 | Out-Null
Write-Host -ForegroundColor DarkGreen "CREANDO VENV..."
python -m venv venv | Out-Null
Write-Host -ForegroundColor DarkGreen "ACTIVANDO VENV..."
.\venv\Scripts\Activate.ps1 | Out-Null
Write-Host -ForegroundColor DarkGreen "UPGRADING PIP..."
python -m pip install --upgrade pip | Out-Null
Write-Host -ForegroundColor DarkGreen "INSTALANDO LIBRERIAS..."
pip install -r requirements.txt --use-pep517 | Out-Null
Write-Host -ForegroundColor DarkGreen "EJECUTANDO PROGRAMA...`n"
Write-Host -ForegroundColor Cyan "###############################`n"
$Host.UI.RawUI.ForegroundColor = "Magenta"
python .\src\main.py
