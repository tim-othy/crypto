from typing import Optional
from ciphers.cipher import Cipher

from encoders.encoder import Encoder

class Xor(Cipher):
    @staticmethod
    def encrypt(key: str, text: str, encoder: Optional[Encoder] = None) -> str:
        return Xor._xor(key, text, encoder)

    @staticmethod
    def decrypt(key: str, text: str, encoder: Optional[Encoder] = None) -> str:
        return Xor._xor(key, text, encoder)

    @staticmethod
    def _xor(key: str, text: str, encoder: Optional[Encoder] = None) -> str:
        _ = lambda buffer: encoder.decode(buffer) if encoder else buffer
        return "".join([chr(ord(a) ^ ord(b)) for a, b in zip(_(Xor._pad_key(key, text)), _(text))])

    @staticmethod
    def _pad_key(key: str, text: str) -> str:
        return (key*len(text))[:len(text)] if len(key) != len(text) else key
