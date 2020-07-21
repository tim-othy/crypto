from collections import OrderedDict
from string import ascii_lowercase
from unittest import TestCase

from distributions.english_distribution import EnglishDistribution
from encoders.hex_encoder import HexEncoder
from estimators.single_char_xor_estimator import SingleCharXorEstimator


class TestSingleCharXorEstimator(TestCase):
    def setUp(self):
        self.estimator = SingleCharXorEstimator(EnglishDistribution)

    def test_bhattacharyya_coefficient_of_distribution_with_itself(self):
        self.assertTrue(
            self.estimator.get_bhattacharyya_coefficient(
                EnglishDistribution.get_char_distribution(), 
                EnglishDistribution.get_char_distribution()
            ) > 0
        )

    def test_mutually_exclusive_distributions(self):
        distribution1 = OrderedDict({'a': 1, 'b': 2, 'c': 3})
        distribution2 = OrderedDict({'x': 1, 'y': 2, 'z': 3})
        self.assertEqual(
            self.estimator.get_bhattacharyya_coefficient(
                distribution1,
                distribution2
            ),
            0
        )

    def test_generate_frequency_distribution_all_letters(self):
        target = OrderedDict({letter: 1 for letter in ascii_lowercase})
        self.assertEqual(self.estimator.generate_char_distribution(ascii_lowercase), target)

    def test_estimate_plaintext_and_key(self):
        source = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        target = ("Cooking MC's like a pound of bacon", "X")

        self.assertEqual(
            self.estimator.estimate_plaintext_key_pair(HexEncoder.decode(source)),
            target
        )
