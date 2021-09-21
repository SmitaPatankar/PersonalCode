# Base64 encoding converts bytes to text
# ASCII is reverse i.e. text to bytes

import base64
encoded_data = base64.b64encode(b"data to be encoded")

print(encoded_data)
# b'ZGF0YSB0byBiZSBlbmNvZGVk'

decoded_data = base64.b64decode("RW5jb2RlIHRoaXMgdGV4dA==")

print("decoded text is ")
# b'Encode this text'
