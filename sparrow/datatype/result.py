from dataclasses import dataclass
from typing import Callable

from sparrow import t, u, v, w, T, V, identity
from sparrow.datatype import DataType
from sparrow.kind.bifunctor import Bifunctor
from sparrow.kind.functor import Functor


class Result(Functor[T], Bifunctor[T, V], DataType):
    def __repr__(self):
        return f"Result({self.value}, {self.error})"

    def __eq__(self: "Result[t, v]", other: "Result[t, v]") -> bool:  # type: ignore
        if isinstance(self, Failure) and isinstance(other, Failure):
            return self.error == other.error
        elif isinstance(self, Success) and isinstance(other, Success):
            return self.value == other.value
        else:
            return False

    def fmap(self: "Result[t, v]", f: Callable[[t], u]) -> "Result[u, v]":
        return Success(f(self.value)) if isinstance(self, Success) else self

    def bimap(
        self: "Result[t, v]", f: Callable[[t], u], g: Callable[[v], w]
    ) -> "Result[u, w]":
        return (
            Success(f(self.value)) # type: ignore
            if isinstance(self, Success)
            else Failure(g(self.error)) # type: ignore
        )

    def first(self: "Result[t, v]", f: Callable[[t], u]) -> "Result[u, v]":
        return self.bimap(f, identity)

    def second(self: "Result[t, v]", f: Callable[[v], w]) -> "Result[t, w]":
        return self.bimap(identity, f)


@dataclass
class Success(Result[T, V]):
    __slots__ = ("value",)

    value: t

    def __repr__(self):
        return f"Success({self.value})"


@dataclass
class Failure(Result[T, V]):
    __slots__ = ("error",)

    error: v

    def __repr__(self):
        return f"Failure({self.error})"
