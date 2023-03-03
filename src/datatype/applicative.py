from abc import ABC, abstractmethod
from typing import Callable, TypeVar

from src.datatype.functor import Functor

T, U = TypeVar("T"), TypeVar("U")


class Applicative(Functor[T], ABC):
    @classmethod
    def pure(cls: "Applicative[T]", value: T) -> "Applicative[T]":
        return cls(value)

    @abstractmethod
    def apply(
        self: "Applicative[T]", f: "Applicative[Callable[[T], U]]"
    ) -> "Applicative[U]":
        pass


def apply(
    f: Applicative[Callable[[T], U]], applicative: Applicative[T]
) -> Applicative[U]:
    return applicative.apply(f)
