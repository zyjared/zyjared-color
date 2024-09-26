import sys
from zyjared_color import color
from zyjared_color.base.styles import STYLES
# from pprint import pprint

# from zyjared_color.html import ColorHtml as Color
# from zyjared_color.html.styles import STYLES

# from zyjared_color.test import ColorTest as Color
# from zyjared_color.test.styles import STYLES


def style(k):
    return getattr(color(k), k)()


def main():
    dic = {}

    for k, v in STYLES.items():
        if isinstance(v, dict):
            for k1, _ in v.items():
                dic[k1] = style(k1)
        else:
            dic[k] = style(k)

    # pprint(dic)
    max_key_len = max([len(k) for k in dic.keys()])
    for k, v in dic.items():
        sys.stdout.write(f"{k:<{max_key_len}}: {v}\n")

    sys.stdout.flush()


if __name__ == "__main__":
    main()
