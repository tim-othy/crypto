from abc import ABC


class Cipher(ABC):
    @staticmethod
    def encrypt(buffer1: str, buffer2: str) -> str:
        pass

    @staticmethod
    def decrypt(buffer1: str, buffer2: str) -> str:
        pass
