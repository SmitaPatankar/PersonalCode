import shutil
try:
    shutil.rmtree("/dev/shm")
except:
    pass

# shutil.move("a.txt", "b.txt")
# shutil.copy("a.txt", "b.txt")
