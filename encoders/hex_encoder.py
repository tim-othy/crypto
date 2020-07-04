from binascii import unhexlify, hexlify

from encoders.byte_encoded import byte_encoded
from encoders.encoder import Encoder


class HexEncoder(Encoder):
    @staticmethod
    @byte_encoded
    def encode(input: str) -> str:
        return hexlify(input)

    @staticmethod
    @byte_encoded
    def decode(hex: str) -> str:
        return unhexlify(hex)
