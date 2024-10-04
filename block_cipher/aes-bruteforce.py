from Crypto.Cipher import AES
#########################
# Bruteforce AES-128    #
# Author: Lorenz Woth   #
#########################

# We know the key is smaller than 2^32, so we can ignore 92 bit in the end
# We shall start at integer 0 and use it as byte value
def brute(plaintext, ciphertext):
    cracked = False
    
    print("[*] Starting bruteforce AES-128.")

    for key in range(2**32):
        # Build 128-bit number out of it (8 * 16 Bit = 128 Bit)
        full_key = key.to_bytes(16, "big") 
        bruteCipher = AES.new(full_key,AES.MODE_ECB)
        decrypted_text = bruteCipher.decrypt(ciphertext)

        if decrypted_text == plaintext:
            print(f"[*] Key found: {full_key.hex()}")
            break
    
    return full_key
    print("[*] Cracking successful.")


def main():

    # We know the following text and cipher text
    p1 = b'Das ist ein Test'
    c1 = bytes.fromhex('68a9df14210b1f79aee2e61da467da17')
    cracked_key = brute(p1, c1)

    # decrypt second cipher with that key
    c2 = bytes.fromhex('91bafe05baec7f2b207724967a5d27df')
    cipher = AES.new(cracked_key,AES.MODE_ECB)
    decrypted = cipher.decrypt(c2)
    print(f"[*] Decrypted c2-ciphertext: {decrypted}")

if __name__ == "__main__":
    main()
