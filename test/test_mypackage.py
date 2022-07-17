import os
import runpy
import sys

from contextlib import contextmanager
from pathlib import Path

import pytest

import mypackage

NOTEBOOK_DIR = Path(__file__).parent.parent / "examples"
NOTEBOOK_SCRIPTS = []
for x in NOTEBOOK_DIR.iterdir():
    if x.is_dir() and (x / "example.py").exists():
        NOTEBOOK_SCRIPTS.append(x.name)


def test_foobar():
    assert mypackage.foo() == "bar"


@contextmanager
def _cwd(directory):
    """Modify working directory and sys.path temporarily"""
    cwd = Path.cwd()
    os.chdir(directory)
    sys.path.insert(0, str(directory))
    yield
    sys.path.pop(0)
    os.chdir(cwd)


@pytest.fixture
def purge_notebook_modules():
    """Remove notebook modules from sys.modules after test.

    Because these modules share common names in each notebook and
    module names have a system-wide scope, import machinery will not
    import new modules for successive notebooks unless old modules of
    same name are removed from sys.modules.

    This might be better served by fixing imports in notebooks using
    importlib.
    """
    SENTINEL = object()
    sys.modules.pop("mock_data", SENTINEL)
    yield
    sys.modules.pop("mock_data", SENTINEL)


@pytest.mark.parametrize("directory", NOTEBOOK_SCRIPTS)
def test_notebook_script(directory: Path, purge_notebook_modules):
    # Run in native directory with modified sys.path for imports to work
    with _cwd(NOTEBOOK_DIR / directory):
        runpy.run_path(str(NOTEBOOK_DIR / directory / "example.py"), run_name="testing")

