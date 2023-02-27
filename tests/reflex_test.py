import contextlib
import io
import logging
from functools import partial
from typing import Callable, TypeVar

import pytest

from src.compose import compose
from src.reflex import reflex

partial_print = partial(print)


cases = [
    ((lambda x: x), 1, 1),
    ((lambda x: x + 1), 2, 3),
]


@pytest.mark.parametrize("call, arg, expected", cases)
def test_reflex_with_partial_print(call, arg, expected):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        reflexed_call = reflex(partial_print)(call)
        assert reflexed_call(arg) == expected
        output = f.getvalue().strip()
        assert output == str(call(arg))


@compose(lambda x: x + 1, lambda x: x * 2, lambda x: x % 3)
def add_one_and_double_return_modulo_three_with_reflex(x):
    return x


cases_with_display = [
    ((lambda x: x), 1, partial_print, 1, "1"),
    ((lambda x: x + 1), 2, lambda v: print(f"Value: {v}"), 3, "Value: 3"),
    (
        compose(lambda x: x + 1, lambda x: x + 1)(lambda x: x + 1),
        2,
        lambda v: print(f"The value is {v} and the type is {type(v)}"),
        5,
        "The value is 5 and the type is <class 'int'>",
    ),
    (
        add_one_and_double_return_modulo_three_with_reflex,
        2,
        lambda v: print(f"The value is {v} and the type is {type(v)}"),
        0,
        "The value is 0 and the type is <class 'int'>",
    ),
]


T, V = TypeVar("T"), TypeVar("V")


@pytest.mark.parametrize(
    "call, arg, displayer, expected_output, expected_display", cases_with_display
)
def test_reflex_with_display(
    call: Callable[[T], V],
    arg: T,
    displayer: Callable[[T], None],
    expected_output: V,
    expected_display: str,
):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        reflexed_call = reflex(displayer)(call)
        assert reflexed_call(arg) == expected_output
        output = f.getvalue().strip()
        assert output == expected_display
