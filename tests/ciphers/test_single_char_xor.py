from unittest import TestCase

from ciphers.single_char_xor import SingleCharXor
from encoders.hex_encoder import HexEncoder


class TestXor(TestCase):
    def test_xor_key_same_length(self):
        key = "ab"
        text = "abcdefg"

        self.assertRaises(ValueError, SingleCharXor.encrypt, key, text)


    def test_xor_key_different_length(self):
        key = "a"
        text = "abcdefg"

        self.assertEqual(SingleCharXor.encrypt(key, text.encode("utf-8")), "\x00\x03\x02\x05\x04\x07\x06")
