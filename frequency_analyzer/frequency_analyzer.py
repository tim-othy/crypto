from collections import OrderedDict
from string import printable

import numpy as np

from ciphers.cipher import Cipher
from distributions.distribution import Distribution


class FrequencyAnalyzer:
    def __init__(self, distribution: Distribution):
        self.char_distribution = distribution.get_char_distribution()
        self.digraph_distribution = distribution.get_digraph_distribution()
        self.alphabet = printable

    def generate_char_distribution(self, text: str) -> OrderedDict:
        return OrderedDict({letter: text.lower().count(letter) for letter in self.char_distribution.keys()})

    def generate_digraph_distribution(self, text: str) -> OrderedDict:
        return OrderedDict({digraph: text.lower().count(digraph) for digraph in self.digraph_distribution.keys()})

    def score_text(self, text: str) -> float:
        char_distance = self.hellinger_distance(self.generate_char_distribution(text), self.char_distribution)
        digraph_distance = self.hellinger_distance(self.generate_digraph_distribution(text), self.digraph_distribution)
        return (char_distance * digraph_distance) / len(text)

    @staticmethod
    def hellinger_distance(text_distribution: OrderedDict, language_distribution) -> float:
        _ = lambda dictionary: np.sqrt(np.array(list(dictionary.values())))
        return np.sqrt(np.sum((_(language_distribution) - _(text_distribution)) ** 2)) / np.sqrt(2)

    def estimate_plaintext_key_pair(self, ciphertext: str, cipher: Cipher) -> list:
        score_text_pairs = {
            self.score_text(cipher.decrypt(letter, ciphertext)): (cipher.decrypt(letter, ciphertext), letter)
            for letter in self.alphabet
        }

        return score_text_pairs[max(score_text_pairs.keys())]
