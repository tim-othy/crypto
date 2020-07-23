from ciphers.stateless_cipher import StatelessCipher


class SingleCharXor(StatelessCipher):
    @staticmethod
    def encrypt(key: str, plaintext: str) -> str:
        return SingleCharXor._xor(key, plaintext)

    @staticmethod
    def decrypt(key: str, ciphertext: str) -> str:
        return SingleCharXor._xor(key, ciphertext)

    @staticmethod
    def _xor(key: str, text: str) -> str:
        if len(key) != 1:
            raise ValueError("Key must be single char")
        return "".join([chr(ord(key) ^ ord(letter)) for letter in text])
