from collections import Counter, OrderedDict
from math import sqrt
from string import printable, ascii_lowercase
from typing import Optional

import numpy as np

from ciphers.cipher import Cipher
from distributions.distribution import Distribution
from encoders.encoder import Encoder

class FrequencyAnalyzer:
    def __init__(self, distribution: Distribution):
        self.char_distribution = distribution.get_char_distribution()
        self.alphabet = printable

    def generate_char_distribution(self, text: str) -> dict:
        return {letter: text.lower().count(letter) for letter in ascii_lowercase}

    def generate_digraph_distribution(self, text: str) -> dict:
        pass

    def score_text(self, text: str) -> float:
        return self.hellinger_distance(self.generate_char_distribution(text), self.char_distribution)/len(text)

    def hellinger_distance(self, text_distribution: OrderedDict, language_distribution) -> float:
        _ = lambda dictionary: np.sqrt(np.array(list(dictionary.values())))
        return np.sqrt(np.sum((_(language_distribution) - _(text_distribution)) ** 2)) / np.sqrt(2)

    def estimate_plaintext_key_pair(self, ciphertext: str, cipher: Cipher, separator: str) -> list:
        score_text_pairs = {
            self.score_text(cipher.decrypt(letter, ciphertext)): (cipher.decrypt(letter, ciphertext), letter)
                for letter in self.alphabet if cipher.decrypt(letter, ciphertext).count(separator) > 0
        }
 
        return score_text_pairs[max(score_text_pairs.keys())]