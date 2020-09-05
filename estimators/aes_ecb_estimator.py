from distributions.distribution import Distribution
from estimators.estimator import Estimator
from utils.utils import partition_string


class AesEcbEstimator(Estimator):
    def __init__(self, distribution: Distribution):
        super().__init__(distribution)
        self.BLOCK_SIZE = 16

    def is_aes_ecb_encrypted(self, ciphertext: str) -> bool:
        blocks = list(partition_string(ciphertext, self.BLOCK_SIZE))
        return len(blocks) != len(set(blocks))

    def estimate_plaintext_key_pair(self, ciphertext: str) -> list:
        pass
