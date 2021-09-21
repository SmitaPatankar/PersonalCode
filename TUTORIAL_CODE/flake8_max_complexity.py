"""
flake8 offers an extra option: –max-complexity, which will emit a warning if the McCabe complexity of a function is
higher than the value. By default it’s deactivated:
$ flake8 --max-complexity 12 coolproject
coolproject/mod.py:1204:1: C901 'selftest' is too complex (14)
This feature is quite useful to detect over-complex code. According to McCabe,
anything that goes beyond 10 is too complex.
"""