from zyjared_color import Color
from zyjared_color.base.styles import STYLES


def styled(k: str):
    text = getattr(Color(k), k)()
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
