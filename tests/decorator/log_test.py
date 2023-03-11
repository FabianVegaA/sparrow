import logging
from typing import Callable, Iterable, Optional

import pytest

from sparrow import T, V, constant, identity
from sparrow.decorator.reflex import critical, debug, error, info, warning


def flat(iterable: Iterable[Iterable[T]]) -> Iterable[T]:
    return (item for sublist in iterable for item in sublist)


cases_info = flat(
    (
        (log_level, identity, 1, 1, None, "1"),
        (log_level, constant(1), 2, 1, None, "1"),
        (
            log_level,
            constant(1),
            2,
            1,
            "The result is {0}",
            "The result is 1",
        ),
    )
    for log_level in (
        logging.DEBUG,
        logging.INFO,
        logging.WARN,
        logging.ERROR,
        logging.CRITICAL,
    )
)


@pytest.mark.parametrize(
    "level_log, call, arg, result, formatted_msg, expected", cases_info
)
def test_loger(
    caplog,
    level_log: int,
    call: Callable[[T], V],
    arg: T,
    result: V,
    formatted_msg: Optional[str],
    expected: str,
):
    loggers = {
        logging.DEBUG: debug,
        logging.INFO: info,
        logging.WARN: warning,
        logging.ERROR: error,
        logging.CRITICAL: critical,
    }
    logging.basicConfig(level=level_log, format="%(message)s")
    with caplog.at_level(level_log):
        decored_call = loggers[level_log](formatted_msg)(call)
        assert decored_call(arg) == result
        assert len(caplog.records) == 1
        log_record: logging.LogRecord = caplog.records[0]
        assert log_record.levelno == level_log
        assert str(log_record.msg) == expected
