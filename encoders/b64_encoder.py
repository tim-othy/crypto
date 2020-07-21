import re
from base64 import b64encode, b64decode

from encoders.byte_encoded import byte_encoded
from encoders.encoder import Encoder


class Base64Encoder(Encoder):
    @staticmethod
    @byte_encoded
    def encode(string: str) -> str:
        return b64encode(string)

    @staticmethod
    def decode(base64: str) -> str:
        data = re.sub(rb'[^a-zA-Z0-9%s]+' % b'+/', b'', base64.encode("utf-8"))
        missing_padding = len(data) % 4
        if missing_padding:
            data += b'=' * (4 - missing_padding)
        return b64decode(data, b'+/').decode("utf-8")
