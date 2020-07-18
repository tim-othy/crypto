from functools import wraps


def byte_encoded(function: callable) -> callable:
    @wraps(function)
    def wrapper(string: str) -> str:
        return function(string.encode("utf-8")).decode("utf-8")
    return wrapper
