def pad_pkcs7(plaintext: str, blocksize: int) -> str:
    pad_length = (blocksize - len(plaintext)) % blocksize
    if pad_length == 0:
        pad_length = blocksize
    return (plaintext.encode('utf-8') + bytes([pad_length] * pad_length)).decode('utf-8')
