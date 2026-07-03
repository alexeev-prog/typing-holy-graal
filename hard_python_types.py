from typing import Callable, TypeVar

T = TypeVar('T')
R = TypeVar('R')


def binder(
    converter: Callable[[int], T]
) -> Callable[[Callable[[T], R]], Callable[[int], R]]:
    def decorator(func: Callable[[T], R]) -> Callable[[int], R]:
        def wrapper(x: int) -> R:
            return func(converter(x))
        return wrapper
    return decorator

int_to_str: Callable[[int], str] = str
bound = binder(int_to_str)


def exclaim(s: str) -> str:
    return f"{s}!"

# bound "превращает" функцию str -> str в функцию int -> str
exclaim_int = bound(exclaim)

result = exclaim_int(42)
print(result)  # "42!"
