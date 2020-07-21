from ciphers.xor import Xor
from distributions.distribution import Distribution
from estimators.estimator import Estimator


class RepeatingKeyXorEstimator(Estimator):
    def __init__(self, distribution: Distribution):
        super().__init__(distribution)

    @staticmethod
    def get_hamming_distance(input1: str, input2: str) -> int:
        return sum([bin(ord(a) ^ ord(b)).count("1") for a, b in zip(input1, input2)])

    @staticmethod
    def get_normalized_hamming_distance(input1: str, input2: str) -> float:
        return RepeatingKeyXorEstimator.get_hamming_distance(input1, input2) / len(input1)

    def estimate_keysize(self, ciphertext: str, lower_keysize_limit: int, upper_keysize_limit: int) -> int:
        keysize_hamming_pairs = {
            keysize: (
                 self.get_normalized_hamming_distance(ciphertext[0: keysize], ciphertext[keysize: keysize * 2]) +
                 self.get_normalized_hamming_distance(ciphertext[keysize: keysize * 2], ciphertext[keysize * 2: keysize * 3]) +
                 self.get_normalized_hamming_distance(ciphertext[keysize * 2: keysize * 3], ciphertext[keysize * 3: keysize * 4])
             ) / 3
            for keysize in range(lower_keysize_limit, upper_keysize_limit + 1)
        }
        return min(keysize_hamming_pairs, key=keysize_hamming_pairs.get)

    def estimate_plaintext_key_pair(self, ciphertext: str) -> list:
        pass