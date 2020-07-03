from binascii import unhexlify, hexlify

from decorators.byte_encoded import byte_encoded
from encoders.base_encoder import BaseEncoder


class HexEncoder(BaseEncoder):
    @staticmethod
    @byte_encoded
    def encode(input: str) -> str:
        return hexlify(input)

    @staticmethod
    @byte_encoded
    def decode(hex: str) -> str:
        return unhexlify(hex)
