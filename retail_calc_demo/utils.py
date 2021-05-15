import pathlib
from typing import Any

from yaml import safe_load

__all__ = [
    'BASE_DIR',
    'yaml_safe_load',
]

BASE_DIR = pathlib.Path(__file__).parent.parent


def yaml_safe_load(file_path: str) -> Any:
    with open(file_path) as f:
        return safe_load(f)
