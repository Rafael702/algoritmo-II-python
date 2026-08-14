import importlib.util
import io
import contextlib
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def load_script(relative_path, name=None):
    """Import a lesson script by path, suppressing its top-level output.

    The scripts live in directories whose names contain spaces and dashes, so
    they cannot be imported as regular modules.
    """
    path = REPO_ROOT / relative_path
    module_name = name or path.stem.replace('-', '_')
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(module)
    finally:
        sys.path.remove(str(path.parent))
    return module


@pytest.fixture(scope='session')
def load():
    return load_script
