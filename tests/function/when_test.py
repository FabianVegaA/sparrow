import pytest

from sparrow.function.when import map_unless, map_when, unless, when

cases_when = [
    (True, lambda x: x + 1, 1, lambda x: x + 2, 2),
    (False, lambda x: x + 1, 1, lambda x: x + 2, 3),
    (True, lambda x: x + 1, 1, None, 2),
    (False, lambda x: x + 1, 1, None, 1),
]


@pytest.mark.parametrize("condition, then, value, otherwise, expected", cases_when)
def test_when(condition, then, value, otherwise, expected):
    if otherwise:
        assert when(condition, then, value, otherwise) == expected
    else:
        assert when(condition, then, value) == expected


@pytest.mark.parametrize("condition, then, value, otherwise, expected", cases_when)
def test_unless(condition, then, value, otherwise, expected):
    if otherwise:
        assert unless(not condition, then, value, otherwise) == expected
    else:
        assert unless(not condition, then, value) == expected


cases_map_when = [
    (
        lambda x: x % 2 == 0,
        lambda x: x + 1,
        [1, 2, 3, 4],
        lambda x: x + 2,
        [3, 3, 5, 5],
        [2, 4, 4, 6],
    ),
    (
        lambda x: x % 2 == 0,
        lambda x: x + 1,
        [1, 2, 3, 4],
        None,
        [1, 3, 3, 5],
        [2, 2, 4, 4],
    ),
]


@pytest.mark.parametrize(
    "predicate, then, value, otherwise, expected_when, expected_unless", cases_map_when
)
def test_map_when(predicate, then, value, otherwise, expected_when, expected_unless):
    if otherwise:
        assert list(map_when(predicate, then, value, otherwise)) == expected_when
        assert list(map_unless(predicate, then, value, otherwise)) == expected_unless
    else:
        assert list(map_when(predicate, then, value)) == expected_when
        assert list(map_unless(predicate, then, value)) == expected_unless
