from functools import wraps
from typing import Callable

from sparrow import t, v, w


def after(
    action: Callable[[v], w]
) -> Callable[[Callable[[t], v]], Callable[[t], w]]:
    """Decorator that applies a function after the decorated function.

    Args:
        action: Function to apply after the decorated function.

    Returns:
        Decorator that applies the action function after the decorated function.

    Example:
        >>> @after(lambda x: x * 2)
        ... def add_1(x):
        ...     return x + 1
        >>> add_1(1)
        4
    """

    def decorator(f: Callable[[t], v]) -> Callable[[t], w]:
        @wraps(f)
        def wrapper(x: t) -> w:
            return action(f(x))

        return wrapper

    return decorator


def before(
    action: Callable[[t], v]
) -> Callable[[Callable[[v], w]], Callable[[t], w]]:
    """Decorator that applies a function before the decorated function.

    Args:
        action: Function to apply before the decorated function.

    Returns:
        Decorator that applies the action function before the decorated function.

    Example:
        >>> @before(int)
        ... def add_1(x):
        ...     return x + 1
        >>> add_1("1")
        2
    """

    def decorator(f: Callable[[v], w]) -> Callable[[t], w]:
        @wraps(f)
        def wrapper(x: t) -> w:
            return f(action(x))

        return wrapper

    return decorator
