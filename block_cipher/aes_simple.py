from Crypto.Cipher import AES

key = 123
full_key = key.to_bytes(16, "big") 

# Our used modes: ECB, CBC, CTR, OFB
cipher = AES.new(full_key, AES.MODE_CBC)

p = b'Hallo Welt!'
ciphertext = cipher.encrypt(p)

print(f'Plaintext: {p} - Key: {key}')
print(f'Ciphertext (HEX): {ciphertext.hex()}')