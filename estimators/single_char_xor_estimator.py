from ciphers.single_char_xor import SingleCharXor
from distributions.distribution import Distribution
from estimators.estimator import Estimator


class SingleCharXorEstimator(Estimator):
    def __init__(self, distribution: Distribution):
        super().__init__(distribution)

    def estimate_plaintext_key_pair(self, ciphertext: str) -> list:
        score_text_pairs = {
            self.score_text(SingleCharXor.decrypt(letter, ciphertext)): (SingleCharXor.decrypt(letter, ciphertext), letter)
            for letter in self.alphabet
        }

        return score_text_pairs[max(score_text_pairs.keys())]
