from functools import partial, wraps
from inspect import signature
from typing import Any, Callable, TypeVar, Union

T = TypeVar("T")


def currify(func: Callable[..., T]) -> Callable[..., Union[Callable[..., T], T]]:
    """
    Currying a function.
    :func: The function to be lazy.
    :return: A function that returns the result of the function.

    :Example:
    >>> @currify
    >>> def add(x: int, y: int) -> int:
    >>>    return x + y
    >>> add_one = add(1)
    >>> add_one(2)
    3
    >>> add_one(3)
    4
    >>> add_one_map = currify(map)(add_one)
    >>> add_one_map([1, 2, 3])
    [2, 3, 4]
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Union[Callable[..., Any], Any]:
        if len(signature(func).parameters) == len(args) + len(kwargs):
            return func(*args, **kwargs)
        elif len(signature(func).parameters) > len(args) + len(kwargs):
            return currify(partial(func, *args, **kwargs))
        raise ValueError("Too many arguments")

    return wrapper
