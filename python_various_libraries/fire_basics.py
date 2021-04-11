import fire


class C:
    def __init__(self, i):
        self.i = i

    def m(self, a, b):
        return (a+b)*self.i


if __name__ == "__main__":
    fire.Fire(C)  # for standalone functions just to fire.Fire()

# python fire_basics.py --i 3 m 5 2
# 21
