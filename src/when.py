from functools import wraps
from typing import Callable, TypeVar

T = TypeVar("T")


def identity(x: T) -> T:
    return x


def when(proposition: Callable[[T], bool]) -> Callable[[T], T]:
    """Return a function that returns its argument if proposition is true, otherwise returns unchanged argument.

    Args:
        proposition (Callable[[T], bool]): A function that takes an argument and returns a boolean.

    Returns:
        Callable[[T], T]: A function that returns its argument if proposition is true, otherwise returns unchanged argument.

    Examples:
        >>> @when(lambda x: x != 0)
        ... def inverse_when_not_zero(x):
        ...     return 1 / x
        >>> divide_by_two(2.0)
        0.5
        >>> divide_by_two(0)
        0
    """

    def decorator(then: Callable[[T], T]) -> Callable[[T], T]:
        @wraps(then)
        def wrapper(x: T) -> T:
            return then(x) if proposition(x) else identity(x)

        return wrapper

    return decorator
