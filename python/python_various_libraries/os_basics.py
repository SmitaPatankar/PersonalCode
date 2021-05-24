import os

print(os.getpid())  # 34608

print(os.environ.get("a"))  # None

# os.mkdir("D:/abc")
# os.makedirs("D:/def/pqr", exist_ok=True)

print(os.listdir("D:/"))  # ['DIR1', 'DIR2']

# last data modification time
# print(os.stat("D:/pqr.txt").st_mtime)  # 1590409968.1900594

# in Octet
# os.chmod("D:/pqr.txt", 0o640)

# os.remove("D:/abc.txt")

print(os.path.exists("D:/"))  # True
print(os.path.isdir("D:/"))  # True
print(os.path.isfile("D:/"))  # False
print(os.path.realpath(__file__))  # D:\GitHub\Python-Programs-For-Various-Libraries\os_basics.py
print(os.path.dirname("D:\\abc\\abc.pyy"))  # D:\abc
print(os.path.join("D:\\", "def", "pqr.txt"))  # D:\def\pqr.txt
print(os.path.abspath(os.path.dirname(__file__)))  # D:\GitHub\Python-Programs-For-Various-Libraries
print(os.path.basename(__file__))  # os_basics.py
print(os.path.getsize(__file__))  # 1192

print(os.stat(__file__).st_size)  # 1192

for root, dirs, files in os.walk("D:/"):
    for d in dirs:
        result = os.path.join(root, d)
        print(result)

# D:/PROJECT STUDY\python random\PyramidTutorial\venv\Include
# D:/PROJECT STUDY\python random\PyramidTutorial\venv\Lib
