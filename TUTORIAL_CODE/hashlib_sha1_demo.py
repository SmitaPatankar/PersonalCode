# sha - secure hash algorithm
# we cannot revert hashing

# encode() : Converts the string into bytes to be acceptable by hash function.
# hexdigest() : Returns the encoded data in hexadecimal format.

import hashlib

print (hashlib.algorithms_guaranteed)
# {'sha512', 'blake2b', 'sha3_256', 'sha224', 'shake_256', 'sha3_384', 'md5', 'sha256', 'sha3_224', 'sha3_512',
# 'sha1', 'blake2s', 'shake_128', 'sha384'}

str = "GeeksforGeeks"

str_encode = str.encode()
print(type(str_encode))  # <class 'bytes'>
print(str_encode)  # b'GeeksforGeeks'

result = hashlib.sha1(str.encode())
print(type(result))  # <class '_hashlib.HASH'>
print(result)  # <sha1 HASH object @ 0x0574CDD0>

print(type(result.hexdigest()))  # <class 'str'>
print(result.hexdigest())  # 4175a37afd561152fb60c305d4fa6026b7e79856
