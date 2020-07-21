from abc import ABC, abstractmethod
from collections import OrderedDict
from math import sqrt
from string import printable

from ciphers.cipher import Cipher
from distributions.distribution import Distribution
from utils.utils import get_intersection


class Estimator(ABC):
    def __init__(self, distribution: Distribution):
        self.alphabet = printable
        self.char_distribution = distribution.get_char_distribution()
        self.digraph_distribution = distribution.get_digraph_distribution()

    @staticmethod
    def get_bhattacharyya_coefficient(text_distribution: OrderedDict, language_distribution: OrderedDict) -> float:
        return sum(
            sqrt(text_distribution[key] * language_distribution[key])
            for key in get_intersection(text_distribution, language_distribution)
        )

    def generate_char_distribution(self, text: str) -> OrderedDict:
        return OrderedDict({letter: text.lower().count(letter) for letter in self.char_distribution.keys()})

    def generate_digraph_distribution(self, text: str) -> OrderedDict:
        return OrderedDict({digraph: text.lower().count(digraph) for digraph in self.digraph_distribution.keys()})

    def score_text(self, text: str) -> float:
        char_distance = self.get_bhattacharyya_coefficient(self.generate_char_distribution(text),
                                                           self.char_distribution)
        digraph_distance = self.get_bhattacharyya_coefficient(
            self.generate_digraph_distribution(text),
            self.digraph_distribution
        )
        return (char_distance * digraph_distance) / len(text)

    @abstractmethod
    def estimate_plaintext_key_pair(self, ciphertext: str) -> list:
        pass
