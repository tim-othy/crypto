import os
from unittest import TestCase

from utils.utils import get_intersection, get_fixtures_path, read_file_chunks


class TestUtils(TestCase):
    def test_get_intersection_dictionary_with_itself(self):
        source = {'a': 1, 'b': 2, 'c': 3}
        target = list(source.keys())
        self.assertEqual(get_intersection(source, source), target)

    def test_read_file_chunks(self):
        with open(os.path.join(get_fixtures_path(), "small_file.txt"), "r") as file:
            chunk_size = 2
            source = read_file_chunks(file, chunk_size=chunk_size)
            test_string = "This is intended to test reading files in chunks."
            target = (test_string[i: i+chunk_size] for i in range(0, len(test_string), chunk_size))

            self.assertEqual(list(source), list(target))
