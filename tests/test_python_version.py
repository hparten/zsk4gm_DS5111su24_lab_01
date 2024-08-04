import sys
import pytest

REQUIRED_PYTHONS = ["3.8", "3.9"]

def test_python_version():
    version = sys.version.split()[0]
    assert any(version.startswith(py) for py in REQUIRED_PYTHONS), f"This project requires Python {REQUIRED_PYTHONS}. Found: {version}"
