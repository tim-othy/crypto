from unittest import TestCase

from utils.utils import get_intersection


class TestUtils(TestCase):
    def test_get_intersection_dictionary_with_itself(self):
        source = {'a': 1, 'b': 2, 'c': 3}
        target = list(source.keys())
        self.assertEqual(get_intersection(source, source), target)