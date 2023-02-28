import pytest

from src.datatype.maybe import Just, Nothing
from src.datatype.result import Failure, Success
from src.decorator.wrap import maybe, result

case_maybe = [
    (lambda *a, **k: 1, Just(1)),
    (lambda *a, **k: None, Nothing),
]


@pytest.mark.parametrize("f, expected", case_maybe)
def test_maybe(f, expected):
    assert maybe(f)(*(1, 2, 3), **{"a": 1, "b": 2}) == expected


try:
    1 / 0
except Exception as e:
    case_result = [
        (lambda *a, **k: 1, Success(1)),
        (lambda *a, **k: 1 / 0, Failure(e)),
    ]


@pytest.mark.parametrize("f, expected", case_result)
def test_result(f, expected):
    res = result(f)(*(1, 2, 3), **{"a": 1, "b": 2})
    if isinstance(res, Failure):
        assert isinstance(expected, Failure) and isinstance(
            expected.error, type(res.error)
        )
    else:
        assert res == expected
