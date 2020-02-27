from unittest import TestCase

from ciphers.xor import xor
from encoders.hex_encoder import HexEncoder


class TestXor(TestCase):
    def test_xor(self):
        hex1 = "1c0111001f010100061a024b53535009181c"
        hex2 = "686974207468652062756c6c277320657965"
        target = "746865206b696420646f6e277420706c6179"

        self.assertEqual(HexEncoder.encode(xor(hex1, hex2, HexEncoder)), target)
