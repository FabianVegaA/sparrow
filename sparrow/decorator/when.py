from functools import wraps
from typing import Callable

from sparrow import t


def when(
    proposition: Callable[[t], bool]
) -> Callable[[Callable[[t], t]], Callable[[t], t]]:
    """Return a function that returns its argument if proposition is true,
    otherwise returns unchanged argument.

    Args:
        proposition (Callable[[t], bool]): A function that takes an argument and
            returns a boolean.

    Returns:
        Callable[[t], t]: A function that returns its argument if proposition is true,
            otherwise returns unchanged argument.

    Examples:
        >>> @when(lambda x: x != 0)
        ... def inverse_when_not_zero(x):
        ...     return 1 / x
        >>> divide_by_two(2.0)
        0.5
        >>> divide_by_two(0)
        0
    """

    def decorator(then: Callable[[t], t]) -> Callable[[t], t]:
        @wraps(then)
        def wrapper(x: t) -> t:
            return then(x) if proposition(x) else x

        return wrapper

    return decorator
