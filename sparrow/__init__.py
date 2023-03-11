from typing import Callable, Type, TypeVar

# Type variables
T = TypeVar("T")
V = TypeVar("V")
U = TypeVar("U")
W = TypeVar("W")

# Type aliases
t = Type[T]
v = Type[V]
u = Type[U]
w = Type[W]


def identity(x: t) -> t:
    """Returns the value passed to it."""
    return x


def constant(x: t) -> Callable[[v], t]:
    """Makes a function that always returns the same value."""

    def f(*args, **kwargs):
        return x

    return f
