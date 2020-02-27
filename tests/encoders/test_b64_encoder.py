from unittest import TestCase
from encoders.b64_encoder import Base64Encoder

class TestBase64Encoder(TestCase):
    def test_encode(self):
        source = "I'm killing your brain like a poisonous mushroom"
        target = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

        self.assertEqual(Base64Encoder.encode(source), target)

    def test_decode(self):
        source = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        target = "I'm killing your brain like a poisonous mushroom"

        self.assertEqual(Base64Encoder.decode(source), target)
