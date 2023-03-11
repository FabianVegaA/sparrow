from sparrow.compose import compose
from sparrow.currify import currify
from sparrow.reflex import reflex
from operator import add, sub, mul, mod
import logging
from sparrow.decorator.reflex import critical, debug, error, info, log, warning

add, sub, mul, mod = map(currify, (add, sub, mul, mod))


@reflex(print)
def add_one_and_print(x):
    return x + 1


add_one_and_print(1)
# output: 2
# display: 2


@reflex(lambda v: print(f"The value is {v} and the type is {type(v)}"))
@compose(add(1), mul(2), mod(3))
def add_one_and_double_return_modulo_three_with_reflex(x):
    return x


add_one_and_double_return_modulo_three_with_reflex(2)
# output: 0
# display: The value is 0 and the type is <class 'int'>


def my_debug(f: callable) -> callable:
    return reflex(lambda v: logging.debug(f"Value: {v}"))(f)

logging.basicConfig(level=logging.DEBUG)


@my_debug
def do_some_stuff(x):
    return 9 << x


do_some_stuff(2)
# output: 36
# display: DEBUG:root:Value: 36




@log(logging.DEBUG, "Value: {0}")
def do_some_stuff(x):
    return 9 << x


# output: 36
# display: DEBUG:root:Value: 36


@critical("This is a critical error for value {0}")
@error("This is an error for value {0}")
@warning("This is a warning for value {0}")
@info("This is an info for value {0}")
@debug("This is a debug for value {0}")
def do_some_stuff(x):
    return 9 << x


# output: 36
# display:
#   DEBUG:root:This is a debug for value 36
#   INFO:root:This is an info for value 36
#   WARNING:root:This is a warning for value 36
#   ERROR:root:This is an error for value 36
#   CRITICAL:root:This is a critical error for value 36
