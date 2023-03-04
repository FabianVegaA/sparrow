from typing import Callable

import pytest

from sparrow import T, V
from sparrow.datatype.maybe import Just, Maybe, Nothing

cases_fmap = [
    (Just(1), lambda x: x + 1, Just(2)),
    (Nothing(), lambda x: x + 1, Nothing()),
]


@pytest.mark.parametrize("maybe, f, expected", cases_fmap)
def test_fmap(maybe: Maybe[T], f: Callable[[T], V], expected: Maybe[V]):
    assert maybe.fmap(f) == expected


cases_pure = [
    (1, Just(1)),
]


@pytest.mark.parametrize("value, expected", cases_pure)
def test_pure(value: T, expected: Maybe[T]):
    assert Maybe.pure(value) == expected


cases_apply = [
    (Just(1), Just(lambda x: x + 1), Just(2)),
    (Just(1), Nothing(), Nothing()),
    (Nothing(), Just(lambda x: x + 1), Nothing()),
]


@pytest.mark.parametrize("maybe, maybe_f, expected", cases_apply)
def test_apply(maybe: Maybe[T], maybe_f: Maybe[Callable[[T], V]], expected: Maybe[V]):
    assert maybe.apply(maybe_f) == expected


cases_bind = [
    (Just(1), lambda x: Just(x + 1), Just(2)),
    (Just(1), lambda x: Nothing(), Nothing()),
    (Nothing(), lambda x: Just(x + 1), Nothing()),
]


@pytest.mark.parametrize("maybe, f, expected", cases_bind)
def test_bind(maybe: Maybe[T], f: Callable[[T], Maybe[V]], expected: Maybe[V]):
    assert maybe.bind(f) == expected
