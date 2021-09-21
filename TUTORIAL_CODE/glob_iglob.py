import glob

# returns interator if files
iter_filenames = glob.iglob("*.py")
for name in iter_filenames:
    print(name)

"""
fire_demo.py
functools_wraps_demo.py
glob_iglob.py
logging_Formatter_converter.py
pkg_resources_demo.py
RotatingHandler_demo.py
"""
