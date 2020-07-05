from unittest import TestCase

from ciphers.xor import Xor
from encoders.hex_encoder import HexEncoder


class TestXor(TestCase):
    def test_xor_key_same_length(self):
        hex1 = "1c0111001f010100061a024b53535009181c"
        hex2 = "686974207468652062756c6c277320657965"
        target = "746865206b696420646f6e277420706c6179"

        self.assertEqual(HexEncoder.encode(Xor.encrypt(hex1, hex2, HexEncoder)), target)

    def test_xor_key_different_length(self):
        key = "a"
        text = "abcdefg"

        self.assertEqual(Xor.encrypt(key, text), "\x00\x03\x02\x05\x04\x07\x06")
