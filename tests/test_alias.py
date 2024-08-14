from zyjared_color import bold, red


def test_alias():
    assert str(bold('test') + '  test') == '\033[1mtest\033[0m  test'
    assert str(red('test')) == '\033[31mtest\033[0m'
