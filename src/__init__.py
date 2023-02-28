from typing import Callable, TypeVar

T, V, U, W = TypeVar("T"), TypeVar("V"), TypeVar("U"), TypeVar("W")


def identity(x: T) -> T:
    """Returns the value passed to it."""
    return x


def constant(x: T) -> Callable[[...], T]:
    """Makes a function that always returns the same value."""

    def f(*args, **kwargs):
        return x

    return f
