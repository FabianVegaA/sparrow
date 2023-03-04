import pytest

from sparrow import constant, identity

cases = [
    (1, 1),
    ("1", "1"),
    (True, True),
    (False, False),
    (None, None),
    ([1, 2, 3], [1, 2, 3]),
    ((1, 2, 3), (1, 2, 3)),
    ({1, 2, 3}, {1, 2, 3}),
    ({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3}),
]


@pytest.mark.parametrize("arg, result", cases)
def test_identity(arg, result):
    assert identity(arg) == result


@pytest.mark.parametrize("arg, result", cases)
def test_constant(arg, result):
    assert constant(arg)() == result


cases_with_args = [
    (1, 2, 1),
    ("1", "2", "1"),
    (True, False, True),
    (False, True, False),
    (None, 1, None),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3]),
    ((1, 2, 3), (4, 5, 6), (1, 2, 3)),
    ({1, 2, 3}, {4, 5, 6}, {1, 2, 3}),
    ({1: 1, 2: 2, 3: 3}, {4: 4, 5: 5, 6: 6}, {1: 1, 2: 2, 3: 3}),
]


@pytest.mark.parametrize("arg, args, result", cases_with_args)
def test_constant_with_args(arg, args, result):
    assert constant(arg)(args) == result
