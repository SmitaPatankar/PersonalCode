import os
# with open('random.bin', 'w') as f:
#     f.write(os.urandom(10))

# Traceback (most recent call last):
#   File "D:/self study/python training/effectivepython/004_write_bytes_to_file.py", line 3, in <module>
#     f.write(os.urandom(10))
# TypeError: write() argument must be str, not bytes

with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))
