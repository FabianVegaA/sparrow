from abc import ABCMeta


class DataType(metaclass=ABCMeta):
    """A data type is a kind of data.

    This is a marker class that is used to mark data types.
    It can be used to make record type or sum types.

    A Data type is not instantiable, because it is a type of data!

    Examples:

    ### Record type
    >>> class MyPair(Generic[A, B], DataType):
    ...     # Here we define a signature for our data type
    ...     pass
    ...
    >>> @dataclass
    ... class Pair(MyPair[A, B]):
    ...     # Here we define the implementation of our data type
    ...     # In this case, we implement a Record type
    ...     first: A
    ...     second: B
    ...
    >>> Pair(1, 2)
    Pair(first=1, second=2)

    ### Sum type
    >>> class Day(DataType):
    ...     pass
    ...
    >>> class Monday(Day):
    ...     pass
    ...
    >>> class Tuesday(Day):
    ...     pass
    ...
    >>> class Wednesday(Day):
    ...     pass
    ...
    >>> class Thursday(Day):
    ...     pass
    ...
    >>> class Friday(Day):
    ...     pass
    ...
    >>> class Saturday(Day):
    ...     pass
    ...
    >>> class Sunday(Day):
    ...     pass
    ...
    >>> Monday()
    Monday()
    >>> Tuesday()
    Tuesday()

    This is really similar to an Enum, but it is useful, because
    we can add values to the data type, and we can add functions
    to the data type allowing us to do generic programming.
    """

    __slots__ = ()

    def __init__(self, *args, **kwargs):
        raise TypeError(
            "The declaration of a data type is not instantiable.\n"
            "For example, you can't do `Maybe(1)`\n"
            "You can only do `Just(1)` or `Nothing()`"
        )
