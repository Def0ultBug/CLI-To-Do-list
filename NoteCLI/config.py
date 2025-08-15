import json
from pathlib import Path
from typing import Any

CONFIG_DEFAULT_PATH = Path.home() / "config" / "todos"
CONFIG = CONFIG_DEFAULT_PATH / "config.json"
TODO_DIR = Path.home() / "todo"
TODO_DIR.mkdir(exist_ok=True)


def load_config(config_path : Path = CONFIG_DEFAULT_PATH):
    if not config_path.exists():
        return {"todo_dir": str(TODO_DIR)}
    with open(config_path, "r") as f:
        data = json.load(f)
    return data



def save_config(config: dict[str, Any])-> None:
    if not CONFIG_DEFAULT_PATH.exists():
        CONFIG_DEFAULT_PATH.mkdir(parents=True,exist_ok=True)
    with open(CONFIG, "w") as file:
        json.dump(config, file)
