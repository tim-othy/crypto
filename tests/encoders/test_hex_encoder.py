from unittest import TestCase
from encoders.hex_encoder import HexEncoder

class TestHexEncoder(TestCase):
    def test_encode(self):
        source = "I'm killing your brain like a poisonous mushroom"
        target = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

        self.assertEqual(HexEncoder.encode(source), target)

    def test_decode(self):
        source = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        target = "I'm killing your brain like a poisonous mushroom"

        self.assertEqual(HexEncoder.decode(source), target)
