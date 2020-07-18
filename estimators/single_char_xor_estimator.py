from ciphers.cipher import Cipher
from distributions.distribution import Distribution
from estimators.estimator import Estimator


class SingleCharXorEstimator(Estimator):
    def __init__(self, distribution: Distribution, cipher: Cipher):
        super().__init__(distribution, cipher)

    def estimate_plaintext_key_pair(self, ciphertext: str) -> list:
        score_text_pairs = {
            self.score_text(self.cipher.decrypt(letter, ciphertext)): (self.cipher.decrypt(letter, ciphertext), letter)
            for letter in self.alphabet
        }

        return score_text_pairs[max(score_text_pairs.keys())]
