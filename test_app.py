# Test on for app.py
"""Test for app.py
"""
import app


def test_one():
    """First test
    """
    assert app.add(3, 4) == 7


def test_two():
    """Second test
    """
    assert app.add(-3, 4) == 1
