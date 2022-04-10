import pytest
def myadd(x,y):
    return x+y
@pytest.mark.parametrize('x,y,target',[(1,2,3),(4,6,10)])
def test_myadd(x,y,target):
    assert myadd(x,y) == target
