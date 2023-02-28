from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar

T, V, W, U = TypeVar("T"), TypeVar("V"), TypeVar("W"), TypeVar("U")


class Bifunctor(Generic[T, U], ABC):
    @abstractmethod
    def bimap(
        self: "Bifunctor[T, V]", f: Callable[[T], U], g: Callable[[V], W]
    ) -> "Bifunctor[U, W]":
        pass

    @abstractmethod
    def first(self: "Bifunctor[T, V]", f: Callable[[T], U]) -> "Bifunctor[U, V]":
        pass

    def second(self: "Bifunctor[T, V]", f: Callable[[V], W]) -> "Bifunctor[T, W]":
        return self.bimap(lambda x: x, f)


def bimap(
    f: Callable[[T], U], g: Callable[[V], W], bifunctor: Bifunctor[T, V]
) -> Bifunctor[U, W]:
    return bifunctor.bimap(f, g)


def first(f: Callable[[T], U], bifunctor: Bifunctor[T, V]) -> Bifunctor[U, V]:
    return bifunctor.first(f)


def second(f: Callable[[V], W], bifunctor: Bifunctor[T, V]) -> Bifunctor[T, W]:
    return bifunctor.second(f)
