from abc import ABC
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

from src import identity
from src.data.bifunctor import Bifunctor
from src.data.functor import Functor

T, V, W, U = TypeVar("T"), TypeVar("V"), TypeVar("W"), TypeVar("U")


class Result(Functor[T], Bifunctor[T, V], ABC):
    def __repr__(self):
        return f"Result({self.value}, {self.error})"

    def __eq__(self: "Result[T, V]", other: "Result[T, V]") -> bool:
        if instance(self, Failure) and isinstance(other, Failure):
            return self.error == other.error
        elif isinstance(self, Success) and isinstance(other, Success):
            return self.value == other.value
        else:
            return False

    def fmap(self: "Result[T]", f: Callable[[T], V]) -> "Result[V]":
        return Success(f(self.value)) if isinstance(self, Success) else self

    def bimap(
        self: "Result[T, V]", f: Callable[[T], U], g: Callable[[V], W]
    ) -> "Result[U, W]":
        return (
            Success(f(self.value))
            if isinstance(self, Success)
            else Failure(g(self.error))
        )

    def first(self: "Result[T, V]", f: Callable[[T], U]) -> "Result[U, V]":
        return self.bimap(f, identity)

    def second(self: "Result[T, V]", f: Callable[[V], W]) -> "Result[T, W]":
        return self.bimap(identity, f)


@dataclass
class Success(Result[T, V]):
    __slots__ = ("value",)

    value: T

    def __repr__(self):
        return f"Success({self.value})"


@dataclass
class Failure(Result[T, V]):
    __slots__ = ("error",)

    error: V

    def __repr__(self):
        return f"Failure({self.error})"
