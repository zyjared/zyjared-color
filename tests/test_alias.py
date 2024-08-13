from zyjared_color import bold, red


def test_alias():
    assert str(bold('test')) == '\033[1mtest\033[0m'
    assert str(red('test')) == '\033[31mtest\033[0m'
