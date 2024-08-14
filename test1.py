from zyjared_color import Color, color

if __name__ == "__main__":
    text0 = Color('Hello World!').red() + '  --- test'
    text1 = f'{Color("Hello World!").blue():<30} -+-+-+- test'

    print(text0)
    print(color(text0))

    print(text1)
    print(color(text1))
