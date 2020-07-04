from typing import Optional
from ciphers.cipher import Cipher

from encoders.encoder import Encoder

class Xor(Cipher):
    @staticmethod
    def _xor(buffer1: str, buffer2: str, encoder: Optional[Encoder] = None) -> str:
        _ = lambda buffer: encoder.decode(buffer) if encoder else buffer
        return "".join([chr(ord(a) ^ ord(b)) for a, b in zip(_(buffer1), _(buffer2))])

    @staticmethod
    def encrypt(buffer1: str, buffer2: str, encoder: Optional[Encoder] = None) -> str:
        return Xor._xor(buffer1, buffer2, encoder)

    @staticmethod
    def decrypt(buffer1: str, buffer2: str, encoder: Optional[Encoder] = None) -> str:
        return Xor._xor(buffer1, buffer2, encoder)
