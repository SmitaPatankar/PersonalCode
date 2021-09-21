import subprocess

proc = subprocess.Popen(['sleep', str(10)])
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('Exit status', proc.poll())

'''
Unfortunately, the timeout parameter is only available in Python 3.3 and later. In earlier versions of Python, you’ll need to use the select built-in module on proc.stdin, proc.stdout, and proc.stderr in order to enforce timeouts on I/O.
'''
