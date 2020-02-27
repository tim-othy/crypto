from binascii import unhexlify, hexlify

from decorators.byte_encoder import byte_encoder
from encoders.base_encoder import BaseEncoder


class HexEncoder(BaseEncoder):
    @staticmethod
    @byte_encoder
    def encode(input: str) -> str:
        return hexlify(input)

    @staticmethod
    @byte_encoder
    def decode(hex: str) -> str:
        return unhexlify(hex)
