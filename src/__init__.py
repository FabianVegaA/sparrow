from typing import Callable, TypeVar

T, V, U, W = TypeVar("T"), TypeVar("V"), TypeVar("U"), TypeVar("W")


def identity(x: T) -> T:
    return x


def constant(x: T) -> Callable[[...], T]:
    def f(*args, **kwargs):
        return x

    return f
