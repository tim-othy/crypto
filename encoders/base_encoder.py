from abc import ABC, abstractmethod


class BaseEncoder(ABC):
    @staticmethod
    def encode(buffer: str) -> str:
        pass

    @staticmethod
    def decode(buffer: str) -> str:
        pass
