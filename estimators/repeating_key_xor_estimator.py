from ciphers.cipher import Cipher
from distributions.distribution import Distribution
from estimators.estimator import Estimator


class RepeatingKeyXorEstimator(Estimator):
    def __init__(self, distribution: Distribution, cipher: Cipher):
        super().__init__(distribution, cipher)

    @staticmethod
    def get_hamming_distance(input1: str, input2: str) -> int:
        return sum([bin(ord(a) ^ ord(b)).count("1") for a, b in zip(input1, input2)])


    def estimate_plaintext_key_pair(self, ciphertext: str) -> list:
        pass