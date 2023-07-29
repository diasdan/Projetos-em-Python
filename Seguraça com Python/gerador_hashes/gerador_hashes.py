import hashlib

string = str(input("Write what you want to hash: "))

result = hashlib.sha1(string.encode('utf-8'))

print(f"String hash: {result.hexdigest()}")
