from operator import add, mod, mul, sub

import pytest

from src.compose import compose
from src.currify import currify

add, sub, mul, mod = map(currify, (add, sub, mul, mod))


@compose(add(1), add(2), add(3), add(4))
def add_10_and_mul_by_100(x):
    return x * 100


cases = [
    (compose(add(1), add(2), add(3), add(4))(mul(1))(1), 11),
    (compose(add(1), add(2), add(3), add(4))(mul(2))(1), 22),
    (compose(mul(2), mul(3), mul(4), mul(5))(add(1))(1), 121),
    (add_10_and_mul_by_100(1), 1100),
    (add_10_and_mul_by_100(2), 1200),
]


@pytest.mark.parametrize("result, expected", cases)
def test_compose(result, expected):
    assert result == expected
