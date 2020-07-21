import os
from unittest import TestCase

import utils.utils as utils


class TestUtils(TestCase):
    def test_get_intersection_dictionary_with_itself(self):
        source = {'a': 1, 'b': 2, 'c': 3}
        target = list(source.keys())
        self.assertEqual(utils.get_intersection(source, source), target)

    def test_read_file_chunks(self):
        with open(os.path.join(utils.get_fixtures_path(), "small_file.txt"), "r") as file:
            chunk_size = 2
            source = utils.read_file_chunks(file, chunk_size=chunk_size)
            test_string = "This is intended to test reading files in chunks."
            target = (test_string[i: i+chunk_size] for i in range(0, len(test_string), chunk_size))

            self.assertEqual(list(source), list(target))

    def test_transpose_blocks(self):
        source = ["1234", "5678", "abcd", "efgh"]
        target = ["15ae", "26bf", "37cg", "48dh"]
        self.assertEqual(utils.transpose_blocks(source), target)

    def test_get_number_partitions(self):
        source = "This is a string"
        chunk_size = 3
        target = 6
        self.assertEqual(utils.get_number_partitions(source, chunk_size), target)

    def test_get_partitions(self):
        source = "This is a string"
        chunk_size = 3
        target = ["Thi", "s i", "s a", " st", "rin", "g"]
        self.assertEqual(list(utils.partition_string(source, chunk_size)), target)
