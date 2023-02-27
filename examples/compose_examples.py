from operator import add, mod, mul, sub

from src.compose import compose
from src.currify import currify

add, sub, mul, mod = map(currify, (add, sub, mul, mod))


@compose(add(1), add(2), add(3), add(4))
def add_10_and_mul_by_100(x):
    return x * 100
