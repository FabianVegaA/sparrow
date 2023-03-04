from typing import Callable, Generic, TypeVar

from src.sparrow import T, U
from src.sparrow.kind import Kind, kind_function


class Functor(Generic[T], Kind):
    @kind_function
    def fmap(self: "Functor[T]", f: Callable[[T], U]) -> "Functor[U]":
        pass


def fmap(f: Callable[[T], U], functor: Functor[T]) -> Functor[U]:
    return functor.fmap(f)
