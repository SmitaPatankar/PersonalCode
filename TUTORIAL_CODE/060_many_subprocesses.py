import subprocess
from time import time


start = time()
procs = []
for _ in range(10):
    proc = subprocess.Popen(['sleep', str('0.1')])
    procs.append(proc)
for proc in procs:
    proc.communicate()
end = time()
print('Finished in %.3f seconds' % (end - start))

# Finished in 0.117 seconds
