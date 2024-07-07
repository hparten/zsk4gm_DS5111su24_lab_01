import sys
import pytest

REQUIRED_PYTHON = "3.9"

def test_python_version():
    version = sys.version.split()[0]
    assert version.startswith(REQUIRED_PYTHON), f"This project requires Python {REQUIRED_PYTHON}+. Found: {version}"
