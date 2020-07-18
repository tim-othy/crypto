from collections import OrderedDict
from string import printable

import numpy as np

from ciphers.cipher import Cipher
from distributions.distribution import Distribution


class Estimator:
    def __init__(self, distribution: Distribution, cipher: Cipher):
        self.alphabet = printable
        self.char_distribution = distribution.get_char_distribution()
        self.cipher = cipher
        self.digraph_distribution = distribution.get_digraph_distribution()


    @staticmethod
    def get_distribution_similarity(text_distribution: OrderedDict, language_distribution) -> float:
        return np.sqrt(np.sum((Estimator.get_similarity_measure(language_distribution) -
                               Estimator.get_similarity_measure(text_distribution)) ** 2)) / np.sqrt(2)

    @staticmethod
    def get_similarity_measure(distribution: OrderedDict):
        return np.sqrt(np.array(list(distribution.values())))

    def generate_char_distribution(self, text: str) -> OrderedDict:
        return OrderedDict({letter: text.lower().count(letter) for letter in self.char_distribution.keys()})

    def generate_digraph_distribution(self, text: str) -> OrderedDict:
        return OrderedDict({digraph: text.lower().count(digraph) for digraph in self.digraph_distribution.keys()})

    def score_text(self, text: str) -> float:
        char_distance = self.get_distribution_similarity(self.generate_char_distribution(text), self.char_distribution)
        digraph_distance = self.get_distribution_similarity(
            self.generate_digraph_distribution(text),
            self.digraph_distribution
        )
        return (char_distance * digraph_distance) / len(text)

    def estimate_plaintext_key_pair(self, ciphertext: str) -> list:
        score_text_pairs = {
            self.score_text(self.cipher.decrypt(letter, ciphertext)): (self.cipher.decrypt(letter, ciphertext), letter)
            for letter in self.alphabet
        }

        return score_text_pairs[max(score_text_pairs.keys())]
