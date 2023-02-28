from abc import ABC
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

from src import T, V
from src.data.functor import Functor


class Maybe(Functor[T], ABC):
    def fmap(self: "Maybe[T]", f: Callable[[T], V]) -> "Maybe[V]":
        return self if isinstance(self, Nothing) else Just(f(self.value))

    def __eq__(self: "Maybe[T]", other: "Maybe[T]") -> bool:
        return isinstance(self, type(other)) and (
            isinstance(self, Nothing) or self.value == other.value
        )

@dataclass
class Just(Maybe[T]):
    __slots__ = ("value",)

    value: T

    def __repr__(self):
        return f"Just({self.value})"


@dataclass
class Nothing(Maybe[T]):
    __slots__ = ()

    def __repr__(self):
        return "Nothing"
