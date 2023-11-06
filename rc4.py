def RC4(key: bytes, message: bytes) -> bytes:
    sbox = key_scheduling(key=key)

    i = j = 0

    ciphertext = b""
    for byte in message:
        keybite, i, j = iterate_keybyte(sbox=sbox, i=i, j=j)

        # XOR the message byte with the keybyte
        ciphertext += bytes([byte ^ keybite])

    return ciphertext

def key_scheduling(key: bytes) -> list:
    j = 0

    sbox = list(range(256))
    for i in range(256):
        j = (j + sbox[i] + key[i % len(key)]) % 256
        (sbox[i], sbox[j]) = (sbox[j], sbox[i])
    
    return sbox

def iterate_keybyte(sbox: list, i: int, j: int) -> bytes:
    i = (i + 1) % 256
    j = (j + sbox[i]) % 256
    (sbox[i], sbox[j]) = (sbox[j], sbox[i])
    keybyte = sbox[(sbox[i] + sbox[j]) % 256]

    return keybyte, i, j

if __name__ == "__main__":
    key = b"\x01\x02\x03\x04\x05\x06\x07" # Change accordingly
    message = b'\x00' * 32 # Change accordingly

    ciphertext = RC4(key=key, message=message)

    print("Ciphertext: ", ciphertext.hex())