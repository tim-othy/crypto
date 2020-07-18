from abc import ABC
from typing import Optional

from encoders.encoder import Encoder


class Cipher(ABC):
    @staticmethod
    def encrypt(buffer1: str, buffer2: str, encoder: Optional[Encoder] = None) -> str:
        pass

    @staticmethod
    def decrypt(buffer1: str, buffer2: str, encoder: Optional[Encoder] = None) -> str:
        pass
