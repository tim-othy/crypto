from ciphers.xor import Xor
from distributions.distribution import Distribution
from estimators.estimator import Estimator
from utils.utils import partition_string, get_number_partitions, pairwise


class RepeatingKeyXorEstimator(Estimator):
    def __init__(self, distribution: Distribution):
        super().__init__(distribution)

    @staticmethod
    def get_hamming_distance(input1: str, input2: str) -> int:
        return sum([bin(ord(a) ^ ord(b)).count("1") for a, b in zip(input1, input2)])

    @staticmethod
    def get_normalized_hamming_distance(input1: str, input2: str) -> float:
        return RepeatingKeyXorEstimator.get_hamming_distance(input1, input2) / len(input1)

    @staticmethod
    def get_average_hamming_distance(ciphertext: str, chunk_size: int) -> float:
        return sum(
            RepeatingKeyXorEstimator.get_normalized_hamming_distance(i, j)
            for i, j in pairwise(partition_string(ciphertext, chunk_size))
        ) / get_number_partitions(ciphertext, chunk_size)

    def estimate_keysize(self, ciphertext: str, lower_keysize_limit: int, upper_keysize_limit: int) -> int:
        keysize_hamming_pairs = {
            keysize: self.get_average_hamming_distance(ciphertext, keysize)
            for keysize in range(lower_keysize_limit, upper_keysize_limit + 1)
        }
        
        return min(keysize_hamming_pairs, key=keysize_hamming_pairs.get)

    def estimate_plaintext_key_pair(self, ciphertext: str) -> list:
        pass