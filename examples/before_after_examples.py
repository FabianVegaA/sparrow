from src.sparrow.before_after import after, before


@after(lambda x: x + 1)
@before(lambda x: x + 2)
def add_6(x):
    return x + 3


add_6(1)  # output: 7


@after(str)
@before(int)
def add_1_then_str(x):
    return x + 1


add_1_then_str(1)  # output: '2'
