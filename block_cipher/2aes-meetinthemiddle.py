from Crypto.Cipher import AES
##############################
# Meet-in-the-middle AES-128 #
# Author: Lorenz Woth        #
##############################

def build_hashtable(hashtable, plaintext):
    print("[*] Building hashtable for all k_1 with E(k_1, m).")
    for key in range(2**16):
        k_1 = key.to_bytes(16, "big") 
        ci = AES.new(k_1,AES.MODE_ECB)
        k1_encrypted_plaintext = ci.encrypt(plaintext)
        # hashtable[k_1] = k1_encrypted_plaintext
        # We store the E(k_1, m) as key with k_1 as value to read the value later on easier.
        hashtable[k1_encrypted_plaintext] = k_1

def brute_c(hashtable, ciphertext):
    print("[*] Brute force on D(k_2, ciphertext) if exists in hash table.")
    for key in range(2**16):
        k_2 = key.to_bytes(16, "big") 
        ci = AES.new(k_2,AES.MODE_ECB)
        k2_decrypted_ciphertext = ci.decrypt(ciphertext)
        if k2_decrypted_ciphertext in hashtable:
            print(f"[*] Candidate found: {k_2.hex()} {hashtable[k2_decrypted_ciphertext].hex()}")

        
def main():
    # p1 =  b'Das ist ein Test'
    # c1 = bytes.fromhex("d011ebb754c1f786b5b8576457c2104e")

    p1 =  b'Wir knacken 2AES'
    c1 = bytes.fromhex("4894511486656bfbf6740a7e80affd5f")

    # build hashtable for all k1 with E(k_1, m)
    hashtable = {}

    # 1. Build hashtable
    build_hashtable(hashtable, p1)
    brute_c(hashtable, c1)

if __name__ == "__main__":
    main()
