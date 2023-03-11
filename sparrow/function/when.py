from typing import Callable, Iterable

from sparrow import identity, t


def when(
    condition: bool,
    then: Callable[[t], t],
    value: t,
    otherwise: Callable[[t], t] = identity,
) -> t:
    """Returns the result of applying the function to the value if the condition
        is true, otherwise returns the value.

    Args:
        condition (bool): The condition to check.
        then (Callable[[t], t]): The function to apply to the value if the condition
            is true.
        value (t): The value to pass to the function.
        otherwise (Callable[[t], t], optional): The function to apply to the value if the
            condition is false. Defaults to identity.

    Returns:
        Callable[[t], t]: The result of applying the function to the value if the
            condition is true, otherwise returns the value.
    """
    return then(value) if condition else otherwise(value)


def unless(
    condition: bool,
    then: Callable[[t], t],
    value: t,
    otherwise: Callable[[t], t] = identity,
) -> t:
    """Returns the result of applying the function to the value if the condition
        is false, otherwise returns the value.

    Args:
        condition (bool): The condition to check.
        then (Callable[[t], t]): The function to apply to the value if the condition
            is false.
        value (t): The value to pass to the function.
        otherwise (Callable[[t], t], optional): The function to apply to the value if the
            condition is true. Defaults to identity.

    Returns:
        Callable[[t], t]: The result of applying the function to the value if the
            condition is false, otherwise returns the value.
    """
    return when(not condition, then, value, otherwise)


def map_when(
    predicate: Callable[[t], bool],
    then: Callable[[t], t],
    value: Iterable[t],
    otherwise: Callable[[t], t] = identity,
) -> Iterable[t]:
    """Returns a sequence of the results of applying the function to the value if the
        condition is true, otherwise returns the value.

    Args:
        predicate (Callable[[t], bool]): The function to check the condition.
        then (Callable[[t], t]): The function to apply to the value if the condition
            is true.
        value (Iterable[t]): The value to pass to the function.
        otherwise (Callable[[t], t], optional): The function to apply to the value if
            the condition is false. Defaults to identity.

    Returns:
        Iterable[t]: A sequence of the results of applying the function to the value if
            the condition is true, otherwise returns the value.
    """
    return map(lambda x: when(predicate(x), then, x, otherwise), value)


def map_unless(
    predicate: Callable[[t], bool],
    then: Callable[[t], t],
    value: Iterable[t],
    otherwise: Callable[[t], t] = identity,
) -> Iterable[t]:
    """Returns a sequence of the results of applying the function to the value if the
        condition is false, otherwise returns the value.

    Args:
        predicate (Callable[[t], bool]): The function to check the condition.
        then (Callable[[t], t]): The function to apply to the value if the condition
            is false.
        value (Iterable[t]): The value to pass to the function.
        otherwise (Callable[[t], t], optional): The function to apply to the value if
            the condition is true. Defaults to identity.

    Returns:
        Iterable[t]: A sequence of the results of applying the function to the value if
            the condition is false, otherwise returns the value.
    """
    return map(lambda x: unless(predicate(x), then, x, otherwise), value)
