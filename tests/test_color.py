from zyjared_color import Color, color
from zyjared_color.base.styles import STYLES


def test_Color():
    for k, v in STYLES.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                ins = getattr(Color(k1), k1)()
                assert ins.text == k1
                assert ins.style[k] == v1
        else:
            ins = getattr(Color(k), k)()
            assert ins.text == k
            assert ins.style[k] == v

        assert len(ins.style) == 1
        assert len(ins.children) == 0


def test_color():
    for k, v in STYLES.items():
        if isinstance(v, dict):
            for k1, v1 in v.items():
                ins = getattr(color(k1), k1)()
                assert ins.text == k1
                assert ins.style[k] == v1
        else:
            ins = getattr(color(k), k)()
            assert ins.text == k
            assert ins.style[k] == v

        assert len(ins.style) == 1
        assert len(ins.children) == 0
