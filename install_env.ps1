pyenv install 3.10.8
pyenv shell 3.10.8
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python .\src\main.py
