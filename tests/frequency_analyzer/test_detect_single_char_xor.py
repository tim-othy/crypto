from binascii import unhexlify, hexlify
from collections import OrderedDict
from string import ascii_lowercase, printable
import os
from unittest import TestCase

from ciphers.single_char_xor import SingleCharXor
from distributions.english_distribution import EnglishDistribution
from encoders.hex_encoder import HexEncoder
from encoders.b64_encoder import Base64Encoder
from frequency_analyzer.frequency_analyzer import FrequencyAnalyzer

class TestDetectSingleCharXor(TestCase):
    def setUp(self):
        self.frequency_analyzer = FrequencyAnalyzer(EnglishDistribution)

    def test_detect_single_char_xor(self):
        with open(f"{self._get_fixtures_path()}/single_char_xor.txt", "r") as file:
            estimate = lambda line: self.frequency_analyzer.estimate_plaintext_key_pair(unhexlify(line.encode("utf-8")), SingleCharXor, " ")
            estimated_plaintext_key_pairs = {estimate(line.strip()): self.frequency_analyzer.score_text(estimate(line.strip())[0]) for line in file }
            
            self.assertEqual(
                max(estimated_plaintext_key_pairs, key=estimated_plaintext_key_pairs.get),
                ('Now that the party is jumping\n', '5')
            )

    def _get_fixtures_path(self):
        return f"{os.getcwd()}/tests/fixtures"