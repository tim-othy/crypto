from binascii import unhexlify
import os
import sys
from unittest import TestCase

from ciphers.single_char_xor import SingleCharXor
from distributions.english_distribution import EnglishDistribution
from estimators.single_char_xor_estimator import SingleCharXorEstimator


class TestDetectSingleCharXor(TestCase):
    def setUp(self):
        self.estimator = SingleCharXorEstimator(EnglishDistribution, SingleCharXor)

    def test_detect_single_char_xor(self):
        with open(f"{self._get_fixtures_path()}/single_char_xor.txt", "r") as file:
            estimate = lambda line: self.estimator.estimate_plaintext_key_pair(
                unhexlify(line.encode("utf-8")).strip().decode("latin-1")
            )
            estimated_plaintext_key_pairs = {
                estimate(line.strip()): self.estimator.score_text(estimate(line.strip())[0]) for line in file}

            self.assertEqual(
                max(estimated_plaintext_key_pairs, key=estimated_plaintext_key_pairs.get),
                ('Now that the party is jumping\n', '5')
            )

    @staticmethod
    def _get_fixtures_path():
        return os.path.join(os.getcwd(), "tests", "fixtures")
