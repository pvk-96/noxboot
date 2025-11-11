"""
config.py — NoxBoot configuration management
Handles loading and saving user preferences (theme, colors, defaults)
"""

import yaml
from pathlib import Path

CONFIG_PATH = Path.home() / ".config/noxboot/config.yaml"

DEFAULT_CONFIG = {
    "theme": "dark",
    "colors": {
        "banner": "magenta",
        "accent": "cyan",
        "text": "white",
    },
    "log_actions": True
}


def load_config():
    """Load config file or create default one if missing."""
    if not CONFIG_PATH.exists():
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_PATH, "r") as f:
        data = yaml.safe_load(f)
    if not data:
        return DEFAULT_CONFIG
    return data


def save_config(cfg):
    """Save user configuration to disk."""
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(cfg, f)
