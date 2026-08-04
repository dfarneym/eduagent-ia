from pathlib import Path
import sys

# Adiciona a pasta src ao PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR / "src"))

#"Vá até a interface e importe a função que inicia a aplicação."
from eduagent.ui.main_page import run_app

if __name__ == "__main__":
    run_app()