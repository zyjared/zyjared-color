# from zyjared_color import Color
# from zyjared_color.base.color import STYLES

from zyjared_color.html import ColorHTML as Color
from zyjared_color.html.html import STYLES


def print_color(k, v):
    title = Color(k).cyan().bold().italic()
    text = getattr(Color(k), k)() + '-12345'
    print(f'{title:<30} -+-+-+- {text}')
    # print(repr(text))


def main():
    for k, v in STYLES.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                print_color(k1, v1)
        else:
            print_color(k, v)


if __name__ == "__main__":
    main()
