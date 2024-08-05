from typing import Any, Dict


def create_alias(class_name: str, styles: Dict[str, Any]):
    temp = f"from .static import Static{class_name}\n\n\n"
    ls = []

    for k, v in styles.items():
        if isinstance(v, dict):
            for k1, _v1 in v.items():
                ls.append(f'{k1} = Static{class_name}.{k1}')
        else:
            ls.append(f'{k} = Static{class_name}.{k}')

    return temp + "\n".join(ls)
