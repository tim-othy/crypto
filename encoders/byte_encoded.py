from functools import wraps


def byte_encoded(function: callable) -> callable:
    @wraps(function)
    def wrapper(string: str) -> str:
        return function(string.encode("ISO-8859-1")).decode("ISO-8859-1")
    return wrapper
