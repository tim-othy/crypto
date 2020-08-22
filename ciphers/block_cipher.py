from abc import ABC, abstractmethod


class BlockCipher(ABC):
    @staticmethod
    @abstractmethod
    def encrypt(key: str, plaintext: str, mode: int) -> str:
        pass

    @staticmethod
    @abstractmethod
    def decrypt(key: str, ciphertext: str, mode: int) -> str:
        pass
