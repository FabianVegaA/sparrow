from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def compose(*fs: Callable[[T], T]) -> Callable[[T], T]:
    """Compose functions.

    Args:
        *fs: Functions to compose.

    Returns:
        A function that composes the given functions.

    Example:
        >>> @compose(add(1), add(2), add(3), add(4))
        ... def add_10_and_mul_by_100(x):
        ...     return x * 100
        >>> add_10_and_mul_by_100(1)
        1100
    """

    def decorator(f: Callable[[T], T]) -> Callable[[T], T]:
        @wraps(f)
        def wrapper(x: T) -> T:
            for g in fs:
                x = g(x)
            return f(x)

        return wrapper

    return decorator
