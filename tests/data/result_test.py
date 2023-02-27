import pytest

from typing import Callable, TypeVar

from src.data.result import Failure, Result, Success

T, V, W, U = TypeVar("T"), TypeVar("V"), TypeVar("W"), TypeVar("U")

cases_functor = [
    (Success(1), lambda x: x + 1, Success(2)),
    (Success(1), lambda x: x - 1, Success(0)),
    (Failure(1), lambda x: x + 1, Failure(1)),
]


@pytest.mark.parametrize("result, f, expected", cases_functor)
def test_fmap(result: Result[T, V], f: Callable[[T], U], expected: Result[U, V]):
    assert result.fmap(f) == expected


cases_bifunctor = [
    (Success(1), lambda x: x + 1, lambda x: x - 1, Success(2)),
    (Success(1), lambda x: x - 1, lambda x: x + 1, Success(0)),
    (Failure(1), lambda x: x + 1, lambda x: x - 1, Failure(0)),
    (Failure(1), lambda x: x - 1, lambda x: x + 1, Failure(2)),
]


@pytest.mark.parametrize("result, f, g, expected", cases_bifunctor)
def test_bimap(
    result: Result[T, V],
    f: Callable[[T], U],
    g: Callable[[V], W],
    expected: Result[U, W],
):
    assert result.bimap(f, g) == expected
