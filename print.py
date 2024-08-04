from zyjared_color import Color
from zyjared_color.color import STYLES


def print_color(k, v):
    title = Color(k).cyan().bold().italic()
    text = getattr(Color(k), k)()
    print(f'{title:<30}:{text}')


def main():
    for k, v in STYLES.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                print_color(k1, v1)
        else:
            print_color(k, v)


if __name__ == "__main__":
    main()
