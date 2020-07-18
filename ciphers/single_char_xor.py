from typing import Optional

from ciphers.cipher import Cipher
from encoders.encoder import Encoder


class SingleCharXor(Cipher):
    @staticmethod
    def encrypt(key: str, text: str, encoder: Optional[Encoder] = None) -> str:
        return SingleCharXor._xor(key, text)

    @staticmethod
    def decrypt(key: str, text: str, encoder: Optional[Encoder] = None) -> str:
        return SingleCharXor._xor(key, text)

    @staticmethod
    def _xor(key: str, text: str, encoder: Optional[Encoder] = None) -> str:
        if len(key) != 1:
            raise ValueError("Key must be single char")
        _ = lambda buffer: encoder.decode(buffer) if encoder else buffer
        return "".join([chr(ord(key) ^ letter) for letter in text])
