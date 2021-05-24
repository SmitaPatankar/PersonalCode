import glob
for filename in glob.iglob("D:/**/*.py", recursive=True):
    print(filename)  # whole paths are printed
