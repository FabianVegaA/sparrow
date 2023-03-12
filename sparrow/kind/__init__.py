from abc import ABCMeta
from functools import partial
from typing import Callable, Optional

from sparrow import constant


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
    func: Optional[Callable] = None, *, has_default: bool = False
) -> Callable:
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
    ...

    """

    # This is a bit of a hack to allow us to receive `has_default` without
    # requiring it to be a keyword argument.
    if isinstance(func, bool):
        has_default = func
        func = None

    def decorator(f: Callable) -> Callable:
        if not has_default:
            f.__isabstractmethod__ = True  # type: ignore
        return f

    # This is a bit of a hack to allow us to us
    # `@kind_function` without parentheses.
    return (
        decorator if func is None else constant(partial(decorator, func))  # type: ignore
    )
