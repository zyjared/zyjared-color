from typing import Optional, List, Callable
import importlib.util
import sys
from pathlib import Path
from .method import create_class, create_class_pyi
from .static import create_static_class, create_static_class_pyi
from .alias import create_alias
from .init import create_init
from zyjared_color import Color, cyan, magenta, dim, green, bold, red, yellow


def log(title, text, extra=''):
    pre = green(' · ').bold()
    if isinstance(title, Color):
        print((f'{pre}{title:<15} {magenta(text)}'))
    else:
        print((f'{pre}{cyan(title):<15} {magenta(text)}'))

    if extra:
        print((f'  {pre.yellow()}{dim(extra)}'))


def load_module(file_path: Path):
    module_name = file_path.stem
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def path_in(path: Path, list: Optional[List[str]]):
    if not list:
        return False
    for i in list:
        if path.name == i:
            return True
    return False


def save_and_check(path: Path, ignore: list[str] = [], callback=Callable[[],str], force=False):
    if path.exists():
        if path_in(path, ignore):
            log(yellow('已忽略'), f'{path}')
            return None

        if not force:
            log('已存在', f'{path}')
            return None

    path.write_text(callback().strip())
    log(green('已创建'), f'{path}')
    return path


def save_before(path: Path):
    style_p = Path(path, "styles.py")
    if not path.is_dir():
        path.mkdir(parents=True)
        log(green('创建目录').bold(), f'{path}')

    if not style_p.exists():
        style_p.write_text("STYLES = {}")
        log(green('已创建'), f'{style_p}', '请在该文件中设置样式后再运行此脚本')
        return None

    style_module = load_module(style_p)
    styles = getattr(style_module, "STYLES", {})
    if not styles:
        log(yellow('未定义'), f'{style_p}', '请在该文件中设置样式后再运行此脚本')
        return None

    return styles


def save_template(path: Path, ignore: list[str] = [], force=False):
    styles = save_before(path)

    if styles is None:
        return

    folder_name = path.stem.lower()
    class_name = f'Color{path.stem.capitalize()}'

    save_and_check(Path(path, "__init__.py"),
                   ignore,
                   lambda: create_init(class_name, folder_name),
                   force)
    save_and_check(Path(path, f"{folder_name}.py"),
                   ignore,
                   lambda: create_class(class_name),
                   force)
    save_and_check(Path(path, f"{folder_name}.pyi"),
                   ignore,
                   lambda: create_class_pyi(class_name, styles),
                   force)
    save_and_check(Path(path, "static.py"),
                   ignore,
                   lambda: create_static_class(class_name, folder_name),
                   force)
    save_and_check(Path(path, "static.pyi"),
                   ignore,
                   lambda: create_static_class_pyi(
                       class_name, folder_name, styles),
                   force)
    save_and_check(Path(path, 'alias.py'),
                   ignore,
                   lambda: create_alias(class_name, styles),
                   force)


def main():
    print(f"\n{bold('生成模板')}")

    if len(sys.argv) == 1:
        log(red('请设置目录名'), '')
        exit(1)

    argv = sys.argv[1:]

    if '--force' in argv:
        force = True
        argv.remove('--force')
    else:
        force = False

    class_name = argv[0]
    if not class_name:
        log(red('缺少参数'), 'class_name')
        exit(1)

    save_template(
        Path(f"zyjared_color/{class_name}"),
        ignore=[f"{class_name}.py"],
        force=force,
    )
