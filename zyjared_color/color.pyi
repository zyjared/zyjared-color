from typing import Self


class Color:

    def __init__(self, text: str | Color) -> None:
        """
        """
        ...

    # styles

    def bold(self) -> Self: ...
    def dim(self) -> Self: ...
    def italic(self) -> Self: ...
    def underline(self) -> Self: ...
    def through(self) -> Self: ...
    def reverse(self) -> Self: ...
    def blink(self) -> Self: ...
    def blink_fast(self) -> Self: ...
    def hidden(self) -> Self: ...

    # fg

    def black(self) -> Self: ...
    def red(self) -> Self: ...
    def green(self) -> Self: ...
    def yellow(self) -> Self: ...
    def blue(self) -> Self: ...
    def magenta(self) -> Self: ...
    def cyan(self) -> Self: ...
    def white(self) -> Self: ...
    def bright_black(self) -> Self: ...
    def bright_red(self) -> Self: ...
    def bright_green(self) -> Self: ...
    def bright_yellow(self) -> Self: ...
    def bright_blue(self) -> Self: ...
    def bright_magenta(self) -> Self: ...
    def bright_cyan(self) -> Self: ...
    def bright_white(self) -> Self: ...

    # bg

    def bg_black(self) -> Self: ...
    def bg_red(self) -> Self: ...
    def bg_green(self) -> Self: ...
    def bg_yellow(self) -> Self: ...
    def bg_blue(self) -> Self: ...
    def bg_magenta(self) -> Self: ...
    def bg_cyan(self) -> Self: ...
    def bg_white(self) -> Self: ...
    def bg_bright_black(self) -> Self: ...
    def bg_bright_red(self) -> Self: ...
    def bg_bright_green(self) -> Self: ...
    def bg_bright_yellow(self) -> Self: ...
    def bg_bright_blue(self) -> Self: ...
    def bg_bright_magenta(self) -> Self: ...
    def bg_bright_cyan(self) -> Self: ...
    def bg_bright_white(self) -> Self: ...
