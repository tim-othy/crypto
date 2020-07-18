from collections import OrderedDict
from string import ascii_lowercase
from unittest import TestCase

from ciphers.xor import Xor
from distributions.english import ENGLISH_DISTRIBUTION
from encoders.hex_encoder import HexEncoder
from frequency_analyzer.frequency_analyzer import FrequencyAnalyzer

class TestFrequencyAnalyzer(TestCase):
    def setUp(self):
        self.frequency_analyzer = FrequencyAnalyzer(ENGLISH_DISTRIBUTION)

    def test_hellinger_distance_of_distribution_with_itself(self):
        self.assertEqual(self.frequency_analyzer.hellinger_distance(ENGLISH_DISTRIBUTION), 0.0)

    def test_generate_frequency_distribution_all_letters(self):
        target = OrderedDict({letter: 1 for letter in ascii_lowercase})
        self.assertEqual(self.frequency_analyzer.generate_frequency_distribution(ascii_lowercase), target)

    def test_estimate_plaintext_and_key(self):
        source = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        target = ("Cooking MC's like a pound of bacon", "X")

        self.assertEqual(self.frequency_analyzer.estimate_plaintext_and_key(HexEncoder.decode(source), Xor, " "), target)
