import pytest

from typing import Callable

from src.data.result import Failure, Result, Success

cases = [
    (Success(1), lambda x: x + 1, Success(2)),
    (Success(1), lambda x: x - 1, Success(0)),
    (Failure(1), lambda x: x + 1, Failure(1)),
]


@pytest.mark.parametrize("result, f, expected", cases)
def test_fmap(result: Result, f: Callable, expected: Result):
    assert result.fmap(f) == expected
