from typing import Callable

from sparrow import T, U
from sparrow.kind import Kind, kind_function
from sparrow.kind.functor import Functor


class Applicative(Functor[T], Kind):
    @classmethod
    def pure(cls: "Applicative[T]", value: T) -> "Applicative[T]":
        return cls(value)

    @kind_function
    def apply(
        self: "Applicative[T]", f: "Applicative[Callable[[T], U]]"
    ) -> "Applicative[U]":
        pass


def apply(
    f: Applicative[Callable[[T], U]], applicative: Applicative[T]
) -> Applicative[U]:
    return applicative.apply(f)
