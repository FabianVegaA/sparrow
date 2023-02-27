from typing import Callable, Iterable, Sequence

from src import T, V, identity


def when(
    condition: bool,
    then: Callable[T, T],
    value: T,
    otherwise: Callable[T, T] = identity,
) -> Callable[T, T]:
    return then(value) if condition else otherwise(value)


def unless(
    condition: bool,
    then: Callable[T, T],
    value: T,
    otherwise: Callable[T, T] = identity,
) -> Callable[T, T]:
    return when(not condition, then, value, otherwise)


def map_when(
    predicate: Callable[T, bool],
    then: Callable[T, V],
    value: Sequence[T],
    otherwise: Callable[T, V] = identity,
) -> Sequence[V]:
    return map(lambda x: when(predicate(x), then, x, otherwise), value)


def map_unless(
    predicate: Callable[T, bool],
    then: Callable[T, V],
    value: Sequence[T],
    otherwise: Callable[T, V] = identity,
) -> Sequence[V]:
    return map(lambda x: unless(predicate(x), then, x, otherwise), value)
