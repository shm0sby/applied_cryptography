from Crypto.Util import strxor
from itertools import combinations
# We get the following ciphertexts
# Given: all lines are encrypted with same cipher stream.

ciphertexts =  [
    b"\x0f'H\x90\x9bH0\x9a\xaek030a)(m\xe0g",
    b'\x0f3;\xf8\x93H0\x9a\xaeq^W+g2\\\x1e\xf5`',
    b'\x0e/U\xe3\xf2A3\xff\xa2\x02:A!mZ*\x04\xf3z',
    b'k2S\xf9\x81;-\xe9\xcbc0\\0l?.m\xf8a',
    b'\nF\\\xff\x9d_D\xf9\xa2r6V6\x04>3\x08\xe5\x08',
    b"\t'_\x90\x9bU7\xff\xa8w,VDg(%\x1d\xe2g"
]

# the following chars have been used:
# - german / english words
# - ASCII-encoded
# - only uppercase letters from A-Z and space "_"

def testing_task1():
    letterA = "A".encode('ascii') # ascii: 41 hex
    space = " ".encode("ascii") # ascii: 20 hex
    
    xor_resultA = strxor.strxor(letterA, space)
    
    print(f"[*] Debug: XOR result of {letterA.hex()} and {space.hex()}: {xor_resultA.decode('ascii')}")
    # uppercase letter XOR space => same letter, but lowercase :)

def testing_task2():
    char1 = "40".encode('ascii')
    char2 = "40".encode("ascii")
    
    xor_resultA = strxor.strxor(char1, char2)
    
    print(f"[*] Debug: XOR result of {char1.hex()} and {char2.hex()}: {xor_resultA.hex()} - {xor_resultA.decode('ascii')}")
    # same numbers XORed return 0


def xor(a, b):
    c = strxor.strxor(a, b)
    print(f"[*] DEBUG: hex c={c.hex()} - byte c={c}")

# Hilfsfunktion zur Darstellung des Ergebnisses in druckbarem Format
def printable_xor_result(xor_result):
    return 

def testing_task3():
    # Get bitwise xor of the given ciphertexts
    # if we get 0 at a position, it means the plaintexts at that position same
    # if we see small chars with XOR with all other ciphertexts, we know there must be the corresponding upper case letter
   
   for i, j in combinations(range(len(ciphertexts)), 2):
        print(f'[*] {i+1} XOR {j+1}:', end=' ')

        xor_result = strxor.strxor(ciphertexts[i], ciphertexts[j])
        
        # print printable chars (between 32 and 122 in ascii table), we ignore that we have some other chars in there
        print(''.join(chr(b) if 32 <= b <= 122 else '_' for b in xor_result))
        if j == 5:
            print("")


# testing_task1()
# testing_task2()
testing_task3()