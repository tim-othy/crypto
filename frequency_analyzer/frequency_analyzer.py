from collections import OrderedDict
from math import sqrt
from string import ascii_lowercase
from typing import Optional

import numpy as np

from ciphers.cipher import Cipher
from encoders.encoder import Encoder

class FrequencyAnalyzer:
    def __init__(self, distribution: dict):
        self.distribution = distribution

    def generate_frequency_distribution(self, text: str) -> dict:
        return {letter: text.lower().count(letter) for letter in ascii_lowercase}

    def score_text(self, text: str) -> float:
        return self.hellinger_distance(self.generate_frequency_distribution(text))

    def hellinger_distance(self, distribution: OrderedDict) -> float:
        _ = lambda dictionary: np.sqrt(np.array(list(dictionary.values())))
        return np.sqrt(np.sum((_(self.distribution) - _(distribution)) ** 2)) / np.sqrt(2)

    def get_most_likely_plaintext(self, ciphertext: str, cipher: Cipher, encoder: Optional[Encoder] = None) -> dict:
        pass