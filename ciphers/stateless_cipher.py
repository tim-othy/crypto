from abc import ABC, abstractmethod


class StatelessCipher(ABC):
    @staticmethod
    @abstractmethod
    def encrypt(key: str, plaintext: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def decrypt(key: str, ciphertext: str) -> str:
        pass
