import hashlib

file1 = 'a.txt'
file2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'The file: {file1} is different from {file2}')
    print(f'{file1} Hash: {hash1.hexdigest()}')
    print(f'{file2} Hash: {hash2.hexdigest()}')
else:
    print(f'The file: {file1} is equal {file2}')
