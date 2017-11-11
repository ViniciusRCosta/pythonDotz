import pytest

def test_basic():
    assert 2*10 == 2*10

def soma(x, w):
    return 3

@pytest.mark.parametrize(
    'resultado, x, y',
      [
          [3,2,1]
      ]
    )

def test_soma(resultado, x, y):
    assert resultado == soma(x,y)



