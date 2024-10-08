from .color import Color
from .styles import STYLES
import re

_STYLES_MAP = {}
for k, v in STYLES.items():
    if isinstance(v, dict):
        for _, v1 in v.items():
            _STYLES_MAP[f'{v1}'] = k
    else:
        _STYLES_MAP[f'{v}'] = k


def _parse(text: str):
    array = []
    sep_reg = r'(.*)(\033\[[\d;]+m)(.*)'
    for v in text.split('\033[0m'):
        if not v:
            continue

        groups = re.findall(sep_reg, v)

        # 无样式文本

        if not groups:
            if v:
                array.append({"text": v})
            continue

        if groups[0][0]:
            array.append({"text": groups[0][0]})

        # 样式与文本

        if groups[0][2]:
            styles_str: str = groups[0][1][2:-1]
            styles = {_STYLES_MAP[v]: v for v in styles_str.split(
                ';') if v in _STYLES_MAP}
            array.append({"text": groups[0][2], "style": styles})

    return array


def _load(text: str):
    '''
    字符串中如果含有样式代码，将被解析为 Color 对象
    '''
    array = _parse(text)
    if len(array) > 1:
        return Color(_children=[Color(v['text'], v.get('style', {})) for v in array])
    else:
        return Color(text, array[0].get('style', {}))


def color(content: str | Color):
    '''
    将字符串转换为 Color 对象

    Example:

    ```python
    # 链式调用
    c1 = color('Hello World!').red().bold()

    # 不用顾及参数是否为 Color 类型
    c2 = color(c1)

    # 保留原始样式，或选择改变
    c3 = color('\\033[33mHello World!\\033[0m test').bold()

    # 拼接
    c4 = c1 + 'test'
    c4.bold() # 拼接后为 Color 对象，可以继续调用

    # format
    c5 = color(f'{c1:<15}test')
    ```
    '''
    if isinstance(content, Color):
        return content
    else:
        return _load(content)


def str_has_style(text: str):
    '''
    检查字符串是否包含 ANSI 转义序列
    '''
    return bool(re.search(r'\033\[\d+', text))


if __name__ == '__main__':
    text = 'abc123\033[33mHello1\033[0mdef456\033[33mHello2\033[0mghi789'
    array = _parse(text)
    print('_parse: ', array)
    print(color(text))

    print('-' * 10)

    text = "test"
    array = _parse(text)
    print('_parse: ', array)
    print(color(text))
