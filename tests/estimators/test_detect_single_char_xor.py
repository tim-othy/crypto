import os
from unittest import TestCase

from ciphers.single_char_xor import SingleCharXor
from distributions.english_distribution import EnglishDistribution
from encoders.hex_encoder import HexEncoder
from estimators.single_char_xor_estimator import SingleCharXorEstimator


class TestDetectSingleCharXor(TestCase):
    def setUp(self):
        self.estimator = SingleCharXorEstimator(EnglishDistribution)

    def test_detect_single_char_xor(self):
        with open(f"{self._get_fixtures_path()}/single_char_xor.txt", "r") as file:
            estimate = lambda line: self.estimator.estimate_plaintext_key_pair(
                HexEncoder.decode(line.strip())
            )
            estimated_plaintext_key_pairs = {
                estimate(line): self.estimator.score_text(estimate(line)[0]) for line in file}

            self.assertEqual(
                max(estimated_plaintext_key_pairs, key=estimated_plaintext_key_pairs.get),
                ('Now that the party is jumping\n', '5')
            )

    @staticmethod
    def _get_fixtures_path():
        return os.path.join(os.getcwd(), "tests", "fixtures")
