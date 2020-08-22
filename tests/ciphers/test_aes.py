from base64 import b64decode
from Crypto.Cipher import AES
import os
from unittest import TestCase

from ciphers.aes import Aes
from encoders.b64_encoder import Base64Encoder
from utils.utils import get_fixtures_path


class TestAes(TestCase):
    def test_aes_ecb_mode(self):
        with open(os.path.join(get_fixtures_path(), "aes_ecb.txt"), "r") as file:
            key = "YELLOW SUBMARINE"
            mode = AES.MODE_ECB

            ciphertext = Base64Encoder.decode(file.read())
            plaintext = Aes.decrypt(key, ciphertext, mode)
            print(plaintext)

            self.assertTrue(plaintext.startswith("I'm back and I'm ringin' the bell"))