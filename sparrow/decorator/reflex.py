from functools import wraps
from typing import Callable, Optional

from sparrow import T, V


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


def log(logger: Callable[[str], None], formatted_msg: Optional[str] = None):
    """Log the result of a function.

    Args:
        logger: A function that takes a string and logs it.
        formatted_msg: A string that is formatted with the result of the function. If None, the result of the function is logged directly.

    Returns:
        A function that logs the result of the function.
    """
    from sparrow.function.when import when

    def decorator(f: Callable[[T], V]) -> Callable[[T], V]:
        @reflex(
            lambda o: logger(
                when(
                    formatted_msg is not None,
                    lambda o: formatted_msg.format(o),
                    o,
                )
            )
        )
        @wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)

        return wrapper

    return decorator


def info(formatted_msg: Optional[str] = None):
    """Log the result of a function at the info level.

    Args:
        formatted_msg: A string that is formatted with the result of the function. If None, the result of the function is logged directly.

    Returns:
        A function that logs the result of the function.
    """
    import logging

    return log(logging.info, formatted_msg)


def debug(formatted_msg: Optional[str] = None):
    """Log the result of a function at the debug level.

    Args:
        formatted_msg: A string that is formatted with the result of the function. If None, the result of the function is logged directly.

    Returns:
        A function that logs the result of the function.
    """
    import logging

    return log(logging.debug, formatted_msg)


def warning(formatted_msg: Optional[str] = None):
    """Log the result of a function at the warn level.

    Args:
        formatted_msg: A string that is formatted with the result of the function. If None, the result of the function is logged directly.

    Returns:
        A function that logs the result of the function.
    """
    import logging

    return log(logging.warning, formatted_msg)


def error(formatted_msg: Optional[str] = None):
    """Log the result of a function at the error level.

    Args:
        formatted_msg: A string that is formatted with the result of the function. If None, the result of the function is logged directly.

    Returns:
        A function that logs the result of the function.
    """
    import logging

    return log(logging.error, formatted_msg)


def critical(formatted_msg: Optional[str] = None):
    """Log the result of a function at the critical level.

    Args:
        formatted_msg: A string that is formatted with the result of the function. If None, the result of the function is logged directly.

    Returns:
        A function that logs the result of the function.
    """
    import logging

    return log(logging.critical, formatted_msg)
