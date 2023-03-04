from abc import ABC
from dataclasses import dataclass
from typing import Callable, Generic, Optional, TypeVar

from src import T, V
from src.datatype import DataType
from src.kind.monad import Monad


class Maybe(Monad[T], DataType):
    def fmap(self: "Maybe[T]", f: Callable[[T], V]) -> "Maybe[V]":
        return self if isinstance(self, Nothing) else Just(f(self.value))

    @classmethod
    def pure(cls: "Maybe[T]", value: Optional[T] = None) -> "Maybe[T]":
        return Just(value) if value is not None else Nothing()

    def apply(self: "Maybe[T]", f: "Maybe[Callable[[T], V]]") -> "Maybe[V]":
        return Nothing() if isinstance(f, Nothing) else self.fmap(f.value)

    def bind(self: "Maybe[T]", f: Callable[[T], "Maybe[V]"]) -> "Maybe[V]":
        return self if isinstance(self, Nothing) else f(self.value)

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
