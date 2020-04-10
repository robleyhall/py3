import sys
print(sys.path)

from app.app1 import incr


def test_incr():
    print(sys.path)
    assert 0 == incr(0)
