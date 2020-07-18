from ciphers.cipher import Cipher
from distributions.distribution import Distribution
from estimators.estimator import Estimator


class RepeatingXorEstimator(Estimator):
    def __init__(self, distribution: Distribution, cipher: Cipher):
        super().__init__(distribution, cipher)
