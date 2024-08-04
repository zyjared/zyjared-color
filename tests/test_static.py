from zyjared_color import ColorStatic, Color
from zyjared_color.color import STYLES


def styled(k: str):
    text = getattr(ColorStatic, k)(k)
    return text


def nested(k: Color, styles: list[str]):
    text = getattr(ColorStatic, k)(k)
    for s in styles:
        text = getattr(ColorStatic, s)(text)
    return text


def test_color():
    for k, v in STYLES.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                ins = styled(k1)
                assert ins.text == k1
                assert ins.style[k] == v1
        else:
            ins = styled(k)
            assert ins.text == k
            assert ins.style[k] == v

        assert len(ins.style) == 1
        assert len(ins.children) == 0


def test_nest():
    styles = ["bold", "italic", "underline"]
    len_tuple = (len(styles), len(styles) + 1)
    for k, v in STYLES.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                ins = nested(k1, styles)
                assert ins.text == k1
                assert ins.style[k] == v1
        else:
            ins = nested(k, styles)
            assert ins.text == k
            assert ins.style[k] == v

        assert len(ins.style) in len_tuple
        assert len(ins.children) == 0
