from abc import ABCMeta
from functools import partial
from typing import Callable, Union

from sparrow import t


class Kind(metaclass=ABCMeta):
    """A kind is a type of types

    You can think of it as a type constructor.

    Examples:
    >>> class Eq(Generic[T], Kind):
    ...     @kind_function
    ...     def eq(self: "Eq[t]", b: "Eq[t]") -> bool:
    ...         pass
    ...
    ...     @kind_function
    ...     def neq(self: "Eq[t]", b: "Eq[t]") -> bool:
    ...         pass
    ...
    >>> class MyEqualibleDatatype(Eq[T], DataType):
    ...     def eq(self: "MyObject[T]", b: "MyObject[T]"):
    ...         return self.value == b.value
    ...
    ...     def neq(self: "MyObject[T]", b: "MyObject[T]"):
    ...         return self.value != b.value
    ...
    >>> @dataclass
    ... class MyObject(MyEqualibleDatatype[T]):
    ...     value: t
    ...
    >>> MyObject(1).eq(MyObject(1))
    True
    >>> MyObject(1).eq(MyObject(2))
    False
    >>> MyObject(1).neq(MyObject(1))
    False
    """

    __slots__ = ()

    def __init__(self, *args, **kwargs):
        raise TypeError(
            "The declaration of a kind is not instantiable, "
            "because it is a type of types."
        )


def kind_function(
    has_default: Union[Callable[..., t], bool] = False
) -> Union[Callable[..., t], Callable[[Callable[..., t]], Callable[..., t]]]:
    """A decorator that marks a function as a kind function

    Examples:
    >>> class Eq(Generic[T], Kind):
    ...     @kind_function
    ...     def eq(self: "Eq[t]", b: "Eq[t]") -> bool:
    ...         pass
    ...
    ...     @kind_function(has_default=True)
    ...     def neq(self: "Eq[t]", b: "Eq[t]") -> bool:
    ...         return not self.eq(b)
    """

    def decorator(f: Callable, has_default: bool) -> Callable:
        if not has_default:
            f.__isabstractmethod__ = True  # type: ignore
        return f

    if isinstance(has_default, bool):
        return partial(decorator, has_default=has_default)
    return decorator(has_default, has_default=False)
