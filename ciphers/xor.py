from typing import Optional

from encoders.base_encoder import BaseEncoder

def xor(buffer1: str, buffer2: str, encoder: Optional[BaseEncoder] = None) -> str:
    _ = lambda buffer: encoder.decode(buffer) if encoder else buffer
    return "".join([chr(ord(a) ^ ord(b)) for a, b in zip(_(buffer1), _(buffer2))])
