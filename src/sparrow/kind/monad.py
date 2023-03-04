from typing import Callable, TypeVar

from src import T, U
from src.kind import Kind, kind_function
from src.kind.applicative import Applicative


class Monad(Applicative[T], Kind):
    @kind_function
    def bind(self: "Monad[T]", f: Callable[[T], "Monad[U]"]) -> "Monad[U]":
        pass


def bind(f: Callable[[T], Monad[U]], monad: Monad[T]) -> Monad[U]:
    return monad.bind(f)
