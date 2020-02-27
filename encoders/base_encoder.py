from abc import ABC, abstractmethod


class BaseEncoder(ABC):
    @staticmethod
    def encode(buffer: str) -> bytes:
        pass

    @staticmethod
    def decode(buffer: bytes) -> bytes:
        pass
