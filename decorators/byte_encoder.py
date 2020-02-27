from functools import wraps


def byte_encoder(function: callable) -> callable:
    """
    Converts function input from string to bytes and function output from bytes to string.
    """
    @wraps(function)
    def wrapper(input: str) -> str:
        return function(input.encode("utf-8")).decode("utf-8")
    return wrapper
