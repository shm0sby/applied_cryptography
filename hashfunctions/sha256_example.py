from Crypto.Hash import SHA256

hash_object = SHA256.new(b"Angewandte")
print(hash_object.hexdigest())

hash_object.update(b'Angewandte Kryptographie')
print(hash_object.hexdigest())