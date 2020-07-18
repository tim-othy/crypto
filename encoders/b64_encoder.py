from base64 import b64encode, b64decode

from encoders.byte_encoded import byte_encoded
from encoders.encoder import Encoder


class Base64Encoder(Encoder):
    @staticmethod
    @byte_encoded
    def encode(string: str) -> str:
        return b64encode(string)

    @staticmethod
    @byte_encoded
    def decode(base64: str) -> str:
        return b64decode(base64)
