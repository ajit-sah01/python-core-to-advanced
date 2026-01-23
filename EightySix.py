import hashlib

password = "admin123"
hash_val = hashlib.sha256(password.encode()).hexdigest()
print(hash_val)
