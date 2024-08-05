from typing import Any, Dict


def create_class(class_name: str): return f"""
from ..core import Style, create_style_method_meta
from .styles import STYLES


class {class_name}(Style, metaclass=create_style_method_meta(STYLES)):

    def _compose_style(self) -> str:
        '''
        self.text and self.style merged result
        '''
        return super()._compose_style()

    def _compose_children(self) -> str:
        '''
        style and self.children merged result

        if you don't need to nest, you can not override this
        '''
        return super()._compose_children()

    def _propagate_style(self) -> None:
        '''
        self.style merged to self.children
        '''
        super()._propagate_style()
"""


def _pyi_head(class_name: str): return f"""
from typing import Self


class {class_name}:

    def __init__(self, text: str | {class_name}) -> None: ...
"""


def _pyi_method(class_name: str, method_name: str):
    return f'def {method_name}(self) -> Self: ...'


def create_class_pyi(class_name: str, styles: Dict[str, Any]):

    methods = ['']
    for k, v in styles.items():
        if isinstance(v, dict):
            for k1, _v1 in v.items():
                methods.append(_pyi_method(class_name, k1))
        else:
            methods.append(_pyi_method(class_name, k))

    return _pyi_head(class_name) + "\n    ".join(methods)
