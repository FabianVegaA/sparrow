from typing import Callable, TypeVar

T, V = TypeVar("T"), TypeVar("V")


def identity(x: T) -> T:
    return x


def constant(x: T) -> Callable[[...], T]:
    def f(*args, **kwargs):
        return x

    return f
