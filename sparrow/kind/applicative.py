from typing import Callable

from sparrow import T, t, u
from sparrow.kind import Kind, kind_function
from sparrow.kind.functor import Functor


class Applicative(Functor[T], Kind):
    @classmethod
    def pure(cls: "Applicative[t]", value: t) -> "Applicative[t]": # type: ignore
        if callable(cls):
            return cls(value)
        raise NotImplementedError(f"The type {cls} does not implement pure.")

    @kind_function
    def apply(
        self: "Applicative[t]", f: "Applicative[Callable[[t], u]]"
    ) -> "Applicative[u]":
        pass


def apply(
    f: Applicative[Callable[[t], u]], applicative: Applicative[t]
) -> Applicative[u]:
    return applicative.apply(f)
