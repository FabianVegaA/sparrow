from abc import ABC, abstractmethod
from typing import Callable, TypeVar

from src.datatype.applicative import Applicative

T, U = TypeVar("T"), TypeVar("U")


class Monad(Applicative[T], ABC):
    @abstractmethod
    def bind(self: "Monad[T]", f: Callable[[T], "Monad[U]"]) -> "Monad[U]":
        pass


def bind(f: Callable[[T], Monad[U]], monad: Monad[T]) -> Monad[U]:
    return monad.bind(f)
