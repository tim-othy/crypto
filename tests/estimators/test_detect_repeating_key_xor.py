import os
from base64 import b64decode
from unittest import TestCase

from ciphers.xor import Xor
from distributions.english_distribution import EnglishDistribution
from encoders.b64_encoder import Base64Encoder
from estimators.repeating_key_xor_estimator import RepeatingKeyXorEstimator
from utils.utils import get_fixtures_path


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
        with open(os.path.join(get_fixtures_path(), "repeating_key_xor.txt"), "r") as file:
            ciphertext = Base64Encoder.decode(file.read())
            keysize = self.estimator.estimate_keysize(ciphertext, 2, 41)
