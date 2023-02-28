from functools import wraps
from typing import Callable, Generic, Optional

from src import T
from src.data.maybe import Just, Maybe, Nothing
from src.data.result import Failure, Result, Success


def maybe(f: Callable[..., Optional[T]]) -> Callable[..., Maybe[T]]:
    """Wraps a function that returns an optional value and returns a Maybe instead.

    Args:
        f (Callable[..., Optional[T]]): The function to wrap.

    Returns:
        Callable[..., Maybe[T]]: The wrapped function.
    """

    @wraps(f)
    def wrapper(*args, **kwargs) -> Maybe[T]:
        result = f(*args, **kwargs)
        return Just(result) if result is not None else Nothing

    return wrapper


def result(f: Callable[..., T]) -> Callable[..., Result[T, Exception]]:
    """Wraps a function that returns a value and catches any exceptions, returning a Result instead.

    Args:
        f (Callable[..., T]): The function to wrap.

    Returns:
        Callable[..., Result[T, Exception]]: The wrapped function.
    """

    @wraps(f)
    def wrapper(*args, **kwargs) -> Result[T, Exception]:
        try:
            return Success(f(*args, **kwargs))
        except Exception as e:
            return Failure(e)

    return wrapper
