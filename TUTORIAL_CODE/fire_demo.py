"""
make cli from any python object
pip install fire
"""

import fire


class C:
    def m(self, n):
        return n*n


if __name__ == '__main__':
    fire.Fire(C)

# python fire_demo.py m 10
# 100
