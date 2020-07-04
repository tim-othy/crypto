from collections import OrderedDict
from string import ascii_lowercase
from unittest import TestCase

from distributions.english import ENGLISH_DISTRIBUTION
from frequency_analyzer.frequency_analyzer import FrequencyAnalyzer

class TestFrequencyAnalyzer(TestCase):
    def setUp(self):
        self.frequency_analyzer = FrequencyAnalyzer(ENGLISH_DISTRIBUTION)

    def test_hellinger_distance_of_distribution_with_itself(self):
        self.assertEqual(self.frequency_analyzer.hellinger_distance(ENGLISH_DISTRIBUTION), 0.0)

    def test_generate_frequency_distribution_all_letters(self):
        target = OrderedDict({letter: 1 for letter in ascii_lowercase})
        self.assertEqual(self.frequency_analyzer.generate_frequency_distribution(ascii_lowercase), target)

