import os
from typing import Generator, TextIO


def get_intersection(dict1: dict, dict2: dict) -> list:
    return [key for key in dict1 if key in dict2]


def get_fixtures_path() -> str:
    return os.path.join(os.getcwd(), "tests", "fixtures")


def read_file_chunks(file: TextIO, chunk_size: int) -> Generator:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        else:
            yield chunk
