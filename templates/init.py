def create_init(class_name: str, folder_name: str): return \
f"""from .{folder_name} import {class_name} # noqa: F401
from .static import Static{class_name} # noqa: F401
from .alias import * # noqa: F403
"""
