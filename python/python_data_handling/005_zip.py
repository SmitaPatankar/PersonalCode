# read big
# https://stackoverflow.com/a/55587252/10064174
from zipfile import ZipFile
with ZipFile("C:/REPOSITORIES/MyRepo/PYTHON/python_big_files_handling/sample.zip") as z:
    names = z.namelist()
    for name in names:
        print(f"{name}--------------->")
        with z.open(name) as f:
            print(f.read())

# write big
# https://stackoverflow.com/a/25650295/10064174
import shutil
shutil.make_archive("C:/REPOSITORIES/MyRepo/.trash/output", "zip", "C:/REPOSITORIES/MyRepo/PYTHON/python_big_files_handling/sample")
