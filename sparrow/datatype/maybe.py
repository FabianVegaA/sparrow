from dataclasses import dataclass
from typing import Callable, Optional

from sparrow import t, v, T
from sparrow.datatype import DataType
from sparrow.kind.monad import Monad


class Maybe(Monad[T], DataType):
    def fmap(self: "Maybe[t]", f: Callable[[t], v]) -> "Maybe[v]":
        return self if isinstance(self, Nothing) else Just(f(self.value))  # type: ignore

    @classmethod
    def pure(cls: "Maybe[t]", value: Optional[t] = None) -> "Maybe[t]":  # type: ignore
        return Just(value) if value is not None else Nothing()  # type: ignore

    def apply(self: "Maybe[t]", f: "Maybe[Callable[[t], v]]") -> "Maybe[v]":
        return Nothing() if isinstance(f, Nothing) else self.fmap(f.value)  # type: ignore

    def bind(self: "Maybe[t]", f: Callable[[t], "Maybe[v]"]) -> "Maybe[v]":
        return self if isinstance(self, Nothing) else f(self.value)  # type: ignore

    def __eq__(self: "Maybe[t]", other: "Maybe[t]") -> bool:  # type: ignore
        return isinstance(self, type(other)) and (
            isinstance(self, Nothing) or self.value == other.value  # type: ignore
        )


@dataclass
class Just(Maybe[T]):
    __slots__ = ("value",)

    value: t

    def __repr__(self):
        return f"Just({self.value})"


@dataclass
class Nothing(Maybe[T]):
    __slots__ = ()

    def __repr__(self):
        return "Nothing"

    def __new__(cls):
        """Nothing is a singleton because it has no state,
        so we can just return the same instance.
        """
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance
