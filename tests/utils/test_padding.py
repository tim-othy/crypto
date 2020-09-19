from unittest import TestCase

from utils.padding import pad_pkcs7


class TestPadding(TestCase):
    def test_pad_pkcs7(self):
        source = "YELLOW SUBMARINE"
        blocksize = 20
        target = "YELLOW SUBMARINE\x04\x04\x04\x04"

        self.assertEqual(pad_pkcs7(source, blocksize), target)
        self.assertEqual(len(pad_pkcs7(source, blocksize)), blocksize)



