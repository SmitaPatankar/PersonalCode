# encode
# https://stackoverflow.com/a/31322359/10064174
"""convert into bytes to save in memory"""
b = 'I am a string'.encode('ASCII')

# decode
# https://stackoverflow.com/a/31322359/10064174
"""decode suitable encoding into human readable format"""
print(b.decode("utf-8"))