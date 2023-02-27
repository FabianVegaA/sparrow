from src.compose import compose
from src.currify import currify
from src.reflex import reflex

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

debug = reflex(lambda v: logging.debug(f"Value: {v}"))

logging.basicConfig(level=logging.DEBUG)


@debug
def do_some_stuff(x):
    return 9 << x


do_some_stuff(2)
# output: 36
# display: DEBUG:root:Value: 36
