from base64 import b64encode, b64decode

from decorators.byte_encoder import byte_encoder
from encoders.base_encoder import BaseEncoder


class Base64Encoder(BaseEncoder):
    @staticmethod
    @byte_encoder
    def encode(input: str) -> str:
        return b64encode(input)

    @staticmethod
    @byte_encoder
    def decode(base64: str) -> str:
        return b64decode(base64)
