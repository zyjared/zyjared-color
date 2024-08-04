from zyjared_color import Color, ColorStatic, blue, red, italic, bold, underline
from zyjared_color.color import STYLES


def print_color(color: Color):
    print(repr(color))


def console(k: str):
    title = ColorStatic.cyan(k).bold().italic().cyan()
    text = italic(k)
    print(bold(title + ": " + text + " " + red("done").bold()))
    return print(f'{title:<30}: ', getattr(text, k)())


if __name__ == "__main__":
    for k, v in STYLES.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                console(k1)
        else:
            console(k)

    print(underline((blue(red(bold('test'))) + " " + red("done").bold())))
