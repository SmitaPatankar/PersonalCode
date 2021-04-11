import tempfile
import time

with tempfile.TemporaryDirectory(dir='/tmp') as d:
    with open("temp.txt", "w") as f:
        f.write("temp")
        time.sleep(10)

# during execution
# /tmp$ ls
# tmpg7jgenkw

# after execution
# directory is gone
