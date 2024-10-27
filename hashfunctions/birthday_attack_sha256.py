from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

"""
Create a SHA-32 message based on SHA-256 and take the last bytes.
Used for practical attack scenario.
"""
def sha32(message):
    h = SHA256.new()
    h.update(message)
    return h.digest()[-4:] # Last 4 byte of hash

"""
Actual attack method to fill the dict and search collisions. :)
"""
def birthday_attack():
    attempts = 0
    dict = {}
    
    while True:
        attempts += 1

        message = get_random_bytes(16)

        h = sha32(message)
        hash_value = h.hex()

        if hash_value in dict:
            # print(f"[*] DEBUG: Found collision!")
            return attempts
        else:
            dict[hash_value] = message


def main():   
    print(f"[*] Starting birthday attack...")
    
    # Simple execution:
    # needed_attempts = birthday_attack()
    # print(f"[*] Needed {needed_attempts} attempts to find collisions.")

    # With 100 repetitions
    trials = 100
    results = [birthday_attack() for _ in range(trials)]
    avg_attempts = sum(results) / trials

    # 1.2 * sqrt(2^32) = 1.2 * 2 ^ (32/2) = 1.2 * 2^16
    expected_value = 1.2 * 2 ** 16

    print(f"[*] Exptected value: {expected_value}")
    print(f"[*]   Average value: {avg_attempts}")

if __name__ == "__main__":
    main()