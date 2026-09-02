import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

configs_dir = _root / "configs"
if not configs_dir.is_dir():
    raise RuntimeError(
        f"Diretorio 'configs/' nao encontrado em {configs_dir}. "
        "Verifique se o deploy inclui todos os arquivos."
    )

from app_core import create_app

app = create_app()
