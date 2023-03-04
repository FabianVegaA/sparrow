from typing import Callable, Iterable, Sequence

from src import T, V, identity


def when(
    condition: bool,
    then: Callable[T, T],
    value: T,
    otherwise: Callable[T, T] = identity,
) -> Callable[T, T]:
    """Returns the result of applying the function to the value if the condition is true, otherwise returns the value.

    Args:
        condition (bool): The condition to check.
        then (Callable[T, T]): The function to apply to the value if the condition is true.
        value (T): The value to pass to the function.
        otherwise (Callable[T, T], optional): The function to apply to the value if the condition is false. Defaults to identity.

    Returns:
        Callable[T, T]: The result of applying the function to the value if the condition is true, otherwise returns the value.
    """
    return then(value) if condition else otherwise(value)


def unless(
    condition: bool,
    then: Callable[T, T],
    value: T,
    otherwise: Callable[T, T] = identity,
) -> Callable[T, T]:
    """Returns the result of applying the function to the value if the condition is false, otherwise returns the value.

    Args:
        condition (bool): The condition to check.
        then (Callable[T, T]): The function to apply to the value if the condition is false.
        value (T): The value to pass to the function.
        otherwise (Callable[T, T], optional): The function to apply to the value if the condition is true. Defaults to identity.

    Returns:
        Callable[T, T]: The result of applying the function to the value if the condition is false, otherwise returns the value.
    """
    return when(not condition, then, value, otherwise)


def map_when(
    predicate: Callable[T, bool],
    then: Callable[T, T],
    value: Sequence[T],
    otherwise: Callable[T, T] = identity,
) -> Sequence[T]:
    """Returns a sequence of the results of applying the function to the value if the condition is true, otherwise returns the value.

    Args:
        predicate (Callable[T, bool]): The function to check the condition.
        then (Callable[T, T]): The function to apply to the value if the condition is true.
        value (Sequence[T]): The value to pass to the function.
        otherwise (Callable[T, T], optional): The function to apply to the value if the condition is false. Defaults to identity.

    Returns:
        Sequence[T]: A sequence of the results of applying the function to the value if the condition is true, otherwise returns the value.
    """
    return map(lambda x: when(predicate(x), then, x, otherwise), value)


def map_unless(
    predicate: Callable[T, bool],
    then: Callable[T, T],
    value: Sequence[T],
    otherwise: Callable[T, T] = identity,
) -> Sequence[T]:
    """Returns a sequence of the results of applying the function to the value if the condition is false, otherwise returns the value.

    Args:
        predicate (Callable[T, bool]): The function to check the condition.
        then (Callable[T, T]): The function to apply to the value if the condition is false.
        value (Sequence[T]): The value to pass to the function.
        otherwise (Callable[T, T], optional): The function to apply to the value if the condition is true. Defaults to identity.

    Returns:
        Sequence[T]: A sequence of the results of applying the function to the value if the condition is false, otherwise returns the value.
    """
    return map(lambda x: unless(predicate(x), then, x, otherwise), value)
