from typing import Callable, TypeVar

from src.sparrow import T, U
from src.sparrow.kind import Kind, kind_function
from src.sparrow.kind.applicative import Applicative


class Monad(Applicative[T], Kind):
    @kind_function
    def bind(self: "Monad[T]", f: Callable[[T], "Monad[U]"]) -> "Monad[U]":
        pass


def bind(f: Callable[[T], Monad[U]], monad: Monad[T]) -> Monad[U]:
    return monad.bind(f)
