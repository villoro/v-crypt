import pytest

from vcrypto import __version__


def test_version():
    assert __version__ == "1.0.4"