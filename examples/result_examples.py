from src.sparrow.data.bifunctor import first, second
from src.sparrow.data.functor import fmap
from src.sparrow.data.result import Failure, Result, Success


def inverse(x: int) -> Result[float, str]:
    return Failure("Cannot divide by zero") if x == 0 else Success(1 / x)


inverse(0)  # Failure("Cannot divide by zero")
inverse(2)  # Success(0.5)
fmap(lambda x: x + 1, inverse(2))  # Success(1.5)


def to_int(x: str) -> Result[int, ValueError]:
    if x.isdigit():
        return Success(int(x))
    return Failure(ValueError(f"{x} is not a digit"))


to_int("1")  # Success(1)
to_int("a")  # Failure(ValueError("a is not a digit"))

value: Result[int, ValueError] = to_int("1")
first(lambda x: x + 1, value)  # Success(2)
second(lambda x: x + 1, value)  # Success(1)

value: Result[int, ValueError] = to_int("a")
first(lambda x: x + 1, value)  # Success(1)
second(lambda e: type(e), value)  # Failure(<class 'ValueError'>)
