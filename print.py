from zyjared_color import Color, color
from zyjared_color.base.styles import STYLES

# from zyjared_color.html import ColorHtml as Color
# from zyjared_color.html.styles import STYLES

# from zyjared_color.test import ColorTest as Color
# from zyjared_color.test.styles import STYLES


def print_color(k, v):
    title = color(k).cyan().bold().italic()
    text: Color = getattr(Color(k), k)() + '-12345'
    print(Color(f'{title:<17} -+-+-+- {text}').bold().yellow())
    print(text.size)


def main():
    for k, v in STYLES.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                print_color(k1, v1)
        else:
            print_color(k, v)


if __name__ == "__main__":
    main()

    content: Color = color('Hello World!').red() + ' --- test'

    text: str = f'{color("Hello World!").blue():<15} -+-+-+- test'
    content: Color = color(text)
