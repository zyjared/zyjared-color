from typing import Dict, Any, TypeVar, Callable
from .core import Style

__all = [
    "Color",
    "STYLES",
    "gen_color_meta"
]

_C = TypeVar("_C", bound="Color")

STYLES = {
    "bold": 1,
    "dim": 2,
    "italic": 3,
    "underline": 4,
    "blink": 5,
    "blink_fast": 6,
    "reverse": 7,
    "hidden": 8,
    "through": 9,

    "fg": {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37,
        "bright_black": 90,
        "bright_red": 91,
        "bright_green": 92,
        "bright_yellow": 93,
        "bright_blue": 94,
        "bright_magenta": 95,
        "bright_cyan": 96,
        "bright_white": 97,
    },
    "bg": {
        "bg_black": 40,
        "bg_red": 41,
        "bg_green": 42,
        "bg_yellow": 43,
        "bg_blue": 44,
        "bg_magenta": 45,
        "bg_cyan": 46,
        "bg_white": 47,
        "bg_bright_black": 100,
        "bg_bright_red": 101,
        "bg_bright_green": 102,
        "bg_bright_yellow": 103,
        "bg_bright_blue": 104,
        "bg_bright_magenta": 105,
        "bg_bright_cyan": 106,
        "bg_bright_white": 107,
    }
}

# -+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+
#
# ColorMeta
#
# -+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+


def _gen_color_method(key: str, value: Any):
    def handler(self: _C):
        self.style[key] = value
        return self
    return handler


def gen_color_meta(styles: Dict[str, Any], callback: Callable[[str, Any], Callable] = _gen_color_method):
    class ColorMeta(type):
        def __new__(cls, name, bases, attrs):
            ncls = super().__new__(cls, name, bases, attrs)
            for k, v in styles.items():
                if isinstance(v, dict):
                    for k1, v1 in v.items():
                        setattr(ncls, k1, callback(k, v1))
                else:
                    setattr(ncls, k, callback(k, v))
            return ncls

    return ColorMeta


# -+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+
#
# Color
#
# -+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+-+-+-+--+-+


class Color(Style, metaclass=gen_color_meta(STYLES)):

    def __to_str_shallow(self):
        if self.text:
            if self.style:
                return f'\033[{';'.join([str(i) for i in self.style.values()])}m{self.text}\033[0m'
            else:
                return self.text
        else:
            return ""

    def __to_str(self):
        if self.children:
            self.propagate()
            return ''.join([c.__to_str_shallow() for c in self.children])
        return self.__to_str_shallow()

    def __str__(self):
        return self.__to_str()

    def __format__(self, format_spec: str):
        return f'{self.__to_str():{format_spec}}'
