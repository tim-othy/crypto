from ciphers.cipher import Cipher


class Xor(Cipher):
    @staticmethod
    def encrypt(key: str, text: str) -> str:
        return Xor._xor(key, text)

    @staticmethod
    def decrypt(key: str, text: str) -> str:
        return Xor._xor(key, text)

    @staticmethod
    def _xor(key: str, text: str) -> str:
        padded_key = Xor._pad_key(key, text)
        return "".join([chr(ord(a) ^ ord(b)) for a, b in zip(padded_key, text)])

    @staticmethod
    def _pad_key(key: str, text: str) -> str:
        return (key * len(text))[:len(text)] if len(key) != len(text) else key
