from abc import ABC


class Encoder(ABC):
    @staticmethod
    def encode(buffer: str) -> str:
        pass

    @staticmethod
    def decode(buffer: str) -> str:
        pass
