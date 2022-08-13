# Test on for app.py
import app


def test_one():
    assert app.add(3, 4) == 7


def test_two():
    assert app.add(-3, 4) == 1
