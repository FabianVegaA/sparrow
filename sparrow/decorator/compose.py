from functools import wraps
from typing import Callable

from sparrow import t


def compose(
    *fs: Callable[[t], t]
) -> Callable[[Callable[[t], t]], Callable[[t], t]]:
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

    def decorator(f: Callable[[t], t]) -> Callable[[t], t]:
        @wraps(f)
        def wrapper(x: t) -> t:
            for g in fs:
                x = g(x)
            return f(x)

        return wrapper

    return decorator
