import os
from unittest import TestCase

from ciphers.xor import Xor
from distributions.english_distribution import EnglishDistribution
from estimators.repeating_key_xor_estimator import RepeatingKeyXorEstimator


class TestDetectRepeatingKeyXor(TestCase):
    def setUp(self):
        self.estimator = RepeatingKeyXorEstimator(EnglishDistribution)

    def test_get_hamming_distance(self):
        input1 = "this is a test"
        input2 = "wokka wokka!!!"
        target = 37

        self.assertEqual(self.estimator.get_hamming_distance(input1, input2), target)

    def test_get_hamming_distance_same_input(self):
        input1 = "this is a test"
        target = 0

        self.assertEqual(self.estimator.get_hamming_distance(input1, input1), target)

    def test_detect_repeating_char_xor(self):
        pass

