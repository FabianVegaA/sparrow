from typing import Callable, Generic

from sparrow import T, t, u
from sparrow.kind import Kind, kind_function


class Functor(Generic[T], Kind):
    @kind_function
    def fmap(self: "Functor[t]", f: Callable[[t], u]) -> "Functor[u]":  # type: ignore
        pass


def fmap(f: Callable[[t], u], functor: Functor[t]) -> Functor[u]:
    return functor.fmap(f)
