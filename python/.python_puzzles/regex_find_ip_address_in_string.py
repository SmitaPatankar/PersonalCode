"""
Input:
IP of my laptop is 192.168.0.1.

Output:
192.168.0.1
"""

import re
def find_ip(string):
    return string.split()[-1][:-1]
print(find_ip("IP of my laptop is 192.168.0.1."))

def find_ip(string):
    return re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", string).group(0)
print(find_ip("IP of my laptop is 192.168.0.1."))
