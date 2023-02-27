from functools import wraps
from typing import Callable, Generic, Optional

from src import T
from src.data.maybe import Just, Maybe, Nothing
from src.data.result import Failure, Result, Success


def maybe(f: Callable[..., Optional[T]]) -> Callable[..., Maybe[T]]:
    @wraps(f)
    def wrapper(*args, **kwargs) -> Maybe[T]:
        result = f(*args, **kwargs)
        return Just(result) if result is not None else Nothing

    return wrapper


def result(f: Callable[..., T]) -> Callable[..., Result[T, Exception]]:
    @wraps(f)
    def wrapper(*args, **kwargs) -> Result[T, Exception]:
        try:
            return Success(f(*args, **kwargs))
        except Exception as e:
            return Failure(e)

    return wrapper
