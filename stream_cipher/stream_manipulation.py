# Task B - Attack on stream cipher

def xor_hex(a, b):
  a = bytes.fromhex(a) 
  b = bytes.fromhex(b)
  return bytes([ x^y for x,y in zip(a, b) ]).hex()

# given cipher (hex)
c1_hex = "73c1250112ac1ee90058ce0392b703324171c58466b05038e7ac"

# given plaintext p1 and target plaintext p2
p1 = "PAY 00000123.45 EUR TO BOB"
p2 = "PAY 01000000.00 EUR TO EVA"

# first parse original and target into hex
p1_hex = p1.encode('ascii').hex()
p2_hex = p2.encode('ascii').hex()

# print(f"[*] Debug: c1  hex: {c1_hex}")

# then we can calc the XOR-diff between original and target plaintext
p_diff_hex = xor_hex(p1_hex, p2_hex)

# now xor it with existing cipher code
c2_hex = xor_hex(p_diff_hex, c1_hex)

print(f"[*] New cipher text: {c2_hex}")

# check if it's correct according to solution 73c1250112ad1ee90059cc0092b306324171c58466b0503ffeaf
c_solution = '73c1250112ad1ee90059cc0092b306324171c58466b0503ffeaf'
assert c2_hex == c_solution