from Crypto.Cipher import AES

from ciphers.block_cipher import BlockCipher


class Aes(BlockCipher):

    @staticmethod
    def encrypt(key: str, plaintext: str, mode: int) -> str:
        pass

    @staticmethod
    def decrypt(key: str, ciphertext: str, mode: int) -> str:
        _ = lambda string: string.encode("latin-1")
        return AES.new(_(key), mode).decrypt(_(ciphertext)).decode("latin-1")
