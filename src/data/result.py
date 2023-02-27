from typing import Callable, Generic, TypeVar

from src.data.functor import Functor
from src.data.bifunctor import Bifunctor

from abc import ABC

from dataclasses import dataclass

T, V, W, U = TypeVar("T"), TypeVar("V"), TypeVar("W"), TypeVar("U")


class Result(Functor[T], Bifunctor[T, V], ABC):
    def __repr__(self):
        return f"Result({self.value}, {self.error})"

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
        return Success(f(self.value)) if isinstance(self, Success) else self

    def second(self: "Result[T, V]", f: Callable[[V], W]) -> "Result[T, W]":
        return self if isinstance(self, Success) else Failure(f(self.error))


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