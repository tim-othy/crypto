import os
from itertools import tee
import typing as T

from numpy.ma import floor


def get_intersection(dict1: dict, dict2: dict) -> list:
    return [key for key in dict1 if key in dict2]


def get_fixtures_path() -> str:
    return os.path.join(os.getcwd(), "tests", "fixtures")


def read_file_chunks(file: T.TextIO, chunk_size: int) -> T.Generator:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        else:
            yield chunk


def partition_string(string: str, chunk_size: int) -> T.Generator:
    return (string[i*chunk_size:(i + 1)*chunk_size] for i in range(int(get_number_partitions(string, chunk_size))))


def get_number_partitions(string: str, chunk_size: int) -> int:
    return floor(len(string)/chunk_size) + 1


def pairwise(iterable: T.Iterable) -> T.Iterator[T.Tuple[T.Any, T.Any]]:
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def transpose_blocks(blocks: list) -> list:
    return ["".join(i) for i in map(list, zip(*blocks))]
