import pathlib
from functools import partial
from typing import Any

from aiohttp.web import json_response
from simplejson import dumps
from yaml import safe_load

__all__ = [
    'BASE_DIR',
    'yaml_safe_load',
    'json_response',
]

BASE_DIR = pathlib.Path(__file__).parent.parent

json_response = partial(json_response, dumps=dumps)


def yaml_safe_load(file_path: str) -> Any:
    with open(file_path) as f:
        return safe_load(f)
