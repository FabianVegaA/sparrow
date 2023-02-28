from src.data.maybe import Maybe
from src.data.result import Result
from src.decorator.when import when
from src.decorator.wrap import maybe, result


@maybe
def inverse(x: int) -> Optional[float]:
    return 1 / x if x != 0 else None


value: Maybe[float] = inverse(2)  # Just(0.5)
value: Maybe[float] = inverse(0)  # Nothing


@result
def inverse(x: int) -> float:
    return 1 / x


value: Result[float, Exception] = inverse(2)  # Success(0.5)
value: Result[float, Exception] = inverse(
    0
)  # Failure(ZeroDivisionError('division by zero'))
