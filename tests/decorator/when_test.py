import pytest

from src.sparrow.decorator.when import when

cases = [
    (lambda x: x != 0, lambda x: 1 / x, 2, 0.5),
    (lambda x: x != 0, lambda x: 1 / x, 0, 0),
    (
        lambda x: x % 2 == 0,
        lambda x: x * 2,
        2,
        4,
    ),
]


@pytest.mark.parametrize("proposition, then, arg, expected", cases)
def test_when(proposition, then, arg, expected):
    assert when(proposition)(then)(arg) == expected
