import subprocess
import shlex

command = 'ls -ltr'
splitted_command = shlex.split(command)
print(splitted_command)  # ['ls', '-ltr']
print(subprocess.check_output(splitted_command))
