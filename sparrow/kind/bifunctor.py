from typing import Callable, Generic

from sparrow import T, U, V, W, t, u, v, w
from sparrow.kind import Kind, kind_function


class Bifunctor(Generic[T, U], Kind):
    @kind_function
    def bimap(
        self: "Bifunctor[t, v]", f: Callable[[t], v], g: Callable[[v], w]
    ) -> "Bifunctor[u, w]":
        pass

    @kind_function
    def first(
        self: "Bifunctor[t, v]", f: Callable[[t], u]
    ) -> "Bifunctor[u, v]":
        pass

    @kind_function
    def second(
        self: "Bifunctor[T, V]", f: Callable[[V], W]
    ) -> "Bifunctor[T, W]":
        return self.bimap(lambda x: x, f)


def bimap(
    f: Callable[[T], U], g: Callable[[V], W], bifunctor: Bifunctor[T, V]
) -> Bifunctor[U, W]:
    return bifunctor.bimap(f, g)


def first(f: Callable[[T], U], bifunctor: Bifunctor[T, V]) -> Bifunctor[U, V]:
    return bifunctor.first(f)


def second(f: Callable[[V], W], bifunctor: Bifunctor[T, V]) -> Bifunctor[T, W]:
    return bifunctor.second(f)
