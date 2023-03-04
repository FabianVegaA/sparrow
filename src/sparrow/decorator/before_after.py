from functools import wraps
from typing import Callable, TypeVar

T, V, W = TypeVar("T"), TypeVar("V"), TypeVar("W")


def after(action: Callable[[V], W]) -> Callable[[Callable[[T], V]], Callable[[T], W]]:
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

    def decorator(f: Callable[[T], V]) -> Callable[[T], W]:
        @wraps(f)
        def wrapper(x: T) -> W:
            return action(f(x))

        return wrapper

    return decorator


def before(action: Callable[[T], V]) -> Callable[[Callable[[V], W]], Callable[[T], W]]:
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

    def decorator(f: Callable[[V], W]) -> Callable[[T], W]:
        @wraps(f)
        def wrapper(x: T) -> W:
            return f(action(x))

        return wrapper

    return decorator
