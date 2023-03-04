from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def reflex(effect: Callable[[T], None]) -> Callable[[T], T]:
    """Reflex the result of a function and apply a side effect.

    Args:
        effect: A function that takes the result of the function and applies a side effect.

    Returns:
        A function that applies the side effect to the result of the function.

    Example:
        >>> @reflex(lambda v: print(f"The value is {v}"))
        ... def add_one_and_print(x):
        ...     return x + 1
        >>> add_one_and_print(1)
        The value is 2
        2
    """

    def decorator(f: Callable[[T], T]) -> Callable[[T], T]:
        @wraps(f)
        def wrapper(x: T) -> T:
            evaluated = f(x)
            effect(evaluated)
            return evaluated

        return wrapper

    return decorator
