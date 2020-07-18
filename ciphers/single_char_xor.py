from ciphers.cipher import Cipher


class SingleCharXor(Cipher):
    @staticmethod
    def encrypt(key: str, text: str) -> str:
        return SingleCharXor._xor(key, text)

    @staticmethod
    def decrypt(key: str, text: str) -> str:
        return SingleCharXor._xor(key, text)

    @staticmethod
    def _xor(key: str, text: str) -> str:
        if len(key) != 1:
            raise ValueError("Key must be single char")
        return "".join([chr(ord(key) ^ letter) for letter in text])
