from typing import Any, Dict


def create_static_class(class_name: str, folder_name: str): return f"""
from .{folder_name} import {class_name}
from .styles import STYLES
from ..core import create_static_style_meta


class Static{class_name}(metaclass=create_static_style_meta({class_name}, STYLES)):
    pass

"""


def _pyi_head(class_name: str, folder_name: str): return f"""
from typing import Union
from .{folder_name} import {class_name}

class Static{class_name}:
"""


def _pyi_method(class_name: str, method_name: str):
    return f"""@staticmethod\n    def {method_name}(text: Union[str | {class_name}]) -> {class_name}: ..."""


def create_static_class_pyi(class_name: str, folder_name: str, styles: Dict[str, Any]):

    methods = ['']
    for k, v in styles.items():
        if isinstance(v, dict):
            for k1, _v1 in v.items():
                methods.append(
                    _pyi_method(class_name, k1))
        else:
            methods.append(_pyi_method(class_name, k))
    return _pyi_head(class_name, folder_name) + "\n    ".join(methods)
