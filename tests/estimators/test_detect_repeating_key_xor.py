import os
from unittest import TestCase

from ciphers.xor import Xor
from distributions.english_distribution import EnglishDistribution
from encoders.b64_encoder import Base64Encoder
from estimators.repeating_key_xor_estimator import RepeatingKeyXorEstimator
from estimators.single_char_xor_estimator import SingleCharXorEstimator
from utils.utils import get_fixtures_path, partition_string, transpose_blocks


class TestDetectRepeatingKeyXor(TestCase):
    def setUp(self):
        self.repeating_key_xor_estimator = RepeatingKeyXorEstimator(EnglishDistribution)
        self.single_char_xor_estimator = SingleCharXorEstimator(EnglishDistribution)

    def test_get_hamming_distance(self):
        input1 = "this is a test"
        input2 = "wokka wokka!!!"
        target = 37

        self.assertEqual(self.repeating_key_xor_estimator.get_hamming_distance(input1, input2), target)

    def test_get_hamming_distance_same_input(self):
        input1 = "this is a test"
        target = 0

        self.assertEqual(self.repeating_key_xor_estimator.get_hamming_distance(input1, input1), target)

    def test_detect_repeating_char_xor(self):
        with open(os.path.join(get_fixtures_path(), "repeating_key_xor.txt"), "r") as file:
            ciphertext = Base64Encoder.decode(file.read())
            plaintext_key_pair = self.repeating_key_xor_estimator.estimate_plaintext_key_pair(ciphertext)

            target_keysize = 29
            target_key = "Terminator X: Bring the noise"
            target_plaintext_first_sentence = "I'm back and I'm ringin' the bell"

            self.assertEqual(len(plaintext_key_pair[1]), target_keysize)
            self.assertEqual(plaintext_key_pair[1], target_key)
            self.assertTrue(plaintext_key_pair[0].startswith(target_plaintext_first_sentence))
