import os
from unittest import TestCase

from distributions.english_distribution import EnglishDistribution
from encoders.hex_encoder import HexEncoder
from estimators.aes_ecb_estimator import AesEcbEstimator
from utils.utils import get_fixtures_path

class TestDetectAesEcb(TestCase):
    def setUp(self):
        self.aes_ecb_estimator = AesEcbEstimator(EnglishDistribution)

    def test_detect_aes_ecb(self):
        with open(os.path.join(get_fixtures_path(), "detect_aes_ecb.txt"), "r") as file:
            lines = file.readlines()
            aes_ecb_detected = lambda line: self.aes_ecb_estimator.is_aes_ecb_encrypted(HexEncoder.decode(line.strip()))
            lines_aes_detected_dict = {
                line.strip(): aes_ecb_detected(line)
                for line in lines if aes_ecb_detected(line)
            }
            
            target = {"d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a": True}
            self.assertEqual(target, lines_aes_detected_dict)
