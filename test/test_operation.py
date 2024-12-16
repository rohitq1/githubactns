from src.math_operations import additon,subtract


def test_add():
    assert additon(2,3)==5
    assert additon(-1,1)==0
    assert subtract(5,3)==2


def test_subtract():
    assert subtract(5,3)==2
    assert subtract(-1,1)==-2
    assert subtract(0,0)==0
    