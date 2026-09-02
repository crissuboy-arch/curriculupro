import json
import os
from pathlib import Path

ROOT = Path(__file__).parent

_config_cache = {}
_default_app_id = None


def _resolve_app_id(app_id=None):
    if app_id is not None:
        return app_id
    global _default_app_id
    if _default_app_id is None:
        _default_app_id = os.getenv("APP_ID", "cv-remix-pro")
    return _default_app_id


def get_config(app_id=None):
    app_id = _resolve_app_id(app_id)
    if app_id not in _config_cache:
        config_path = ROOT / "configs" / f"{app_id}.json"
        if not config_path.is_file():
            raise FileNotFoundError(
                f"Configuracao nao encontrada: {config_path}. "
                f"Crie o arquivo configs/{app_id}.json ou ajuste a APP_ID."
            )
        with open(config_path, "r", encoding="utf-8") as f:
            _config_cache[app_id] = json.load(f)
    return _config_cache[app_id]


def reload_config(app_id=None):
    app_id = _resolve_app_id(app_id)
    _config_cache.pop(app_id, None)
    return get_config(app_id)


def list_configs():
    configs_dir = ROOT / "configs"
    configs = []
    if configs_dir.is_dir():
        for fpath in sorted(configs_dir.glob("*.json")):
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                branding = data.get("branding", {})
                configs.append({
                    "app_id": data.get("app_id", fpath.stem),
                    "app_name": branding.get("app_name", fpath.stem),
                    "short_name": branding.get("short_name", fpath.stem),
                    "description": data.get("hero", {}).get("subtitle", ""),
                    "icon": branding.get("favicon_emoji", ""),
                    "color": data.get("colors", {}).get("primary", "#2563EB"),
                    "assistant_name": branding.get("assistant_name", ""),
                })
            except Exception:
                pass
    return configs


CONFIG = get_config()
BRANDING = CONFIG.get("branding", {})
SIDEBAR_ITEMS = CONFIG.get("sidebar", {}).get("items", {})
SIDEBAR_CATEGORIES = CONFIG.get("sidebar", {}).get("categories", [])
ACTION_BUTTONS = CONFIG.get("action_buttons", [])
PLATFORM_PATTERNS = CONFIG.get("url_analysis", {}).get("platform_patterns", [])
PRODUCT_TYPE_KEYWORDS = CONFIG.get("url_analysis", {}).get("product_type_keywords", {})
PROMPTS = CONFIG.get("prompts", {})
SYSTEM_PROMPTS = CONFIG.get("system_prompts", {})
UPLOADS = CONFIG.get("uploads", {})
TOOLS = CONFIG.get("tools", [])
IMPORTS = CONFIG.get("imports", [])
NICHES = CONFIG.get("niches", [])
DASHBOARD_METRICS = CONFIG.get("dashboard_metrics", [])
HERO = CONFIG.get("hero", {})
COLORS = CONFIG.get("colors", {})
IMPORT_TAGS = CONFIG.get("import_tags", [])
MODELS = APP_MODELS = CONFIG.get("models", {})
URL_TYPES = CONFIG.get("url_analysis", {}).get("types", [])
