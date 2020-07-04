from abc import ABC, abstractmethod


class Encoder(ABC):
    @staticmethod
    def encode(buffer: str) -> str:
        pass

    @staticmethod
    def decode(buffer: str) -> str:
        pass
