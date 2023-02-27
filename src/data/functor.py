from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar

T, U = TypeVar("T"), TypeVar("U")


class Functor(Generic[T], ABC):
    @abstractmethod
    def fmap(self: "Functor[T]", f: Callable[[T], U]) -> "Functor[U]":
        pass


def fmap(f: Callable[[T], U], functor: Functor[T]) -> Functor[U]:
    return functor.fmap(f)