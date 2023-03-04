import pytest

from sparrow.decorator.before_after import after, before

cases_before = [
    (lambda x: x + 1, lambda x: x + 2, 1, 4),
    (int, lambda x: x + 2, "1", 3),
]


@pytest.mark.parametrize(
    "before_action, function, input, expected", cases_before
)
def test_before(before_action, function, input, expected):
    assert before(before_action)(function)(input) == expected


cases_after = [
    (lambda x: x + 1, lambda x: x + 2, 1, 4),
    (int, lambda x: x + 1, "1", 2),
]


@pytest.mark.parametrize(
    "function, after_action, input, expected", cases_after
)
def test_after(function, after_action, input, expected):
    assert after(after_action)(function)(input) == expected


cases_before_after = [
    (lambda x: x + 1, lambda x: x + 2, lambda x: x + 3, 1, 7),
    (int, lambda x: x + 1, lambda x: x + 2, "1", 4),
    (str, lambda x: x + "1", lambda x: int(x + "2"), 0, 12),
]


@pytest.mark.parametrize(
    "before_action, function, after_action, input, expected",
    cases_before_after,
)
def test_before_after(before_action, function, after_action, input, expected):
    assert (
        after(after_action)(before(before_action)(function))(input) == expected
    )
