from unittest import TestCase

from ciphers.xor import Xor
from encoders.hex_encoder import HexEncoder


class TestXor(TestCase):
    def test_xor_key_same_length(self):
        hex1 = "1c0111001f010100061a024b53535009181c"
        hex2 = "686974207468652062756c6c277320657965"
        target = "746865206b696420646f6e277420706c6179"

        self.assertEqual(HexEncoder.encode(Xor.encrypt(hex1, hex2, HexEncoder)), target)

    def test_repeating_key_xor(self):
        plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
        key = "ICE"
        target="0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

        self.assertEqual(HexEncoder.encode(Xor.encrypt(key, plaintext)), target)
