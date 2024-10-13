from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#############################
# Encryption with AES-CBC   #
# and pkcs7 padding         #
# # Task 3.9.F              #
# Author: Lorenz Woth       #
#############################

def cbc_enc(key,iv,message):
    print('[*] Doing cbc enccryption...')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(message, 16, 'pkcs7'))

def cbc_dec(key,iv,message):
    print('[*] Doing cbc decryption...')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(message), 16, 'pkcs7')


def main():
    print('[*] Performing Encrytion with AES-CBC and pkcs7 padding.')
    
    k = b'einszweidreivier'
    iv = b'1234567890abcdef'
    
    c = cbc_enc(k,iv,b'Hallo Welt')
    print(f'[*] Ciphertext: {c.hex()}')
    
    pt = cbc_dec(k,iv,c)
    print(f'[*] Plaintext: {pt}')

if __name__ == "__main__":
    main()