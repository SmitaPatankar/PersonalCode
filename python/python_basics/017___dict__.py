class C:
    def __init__(self):
        self.x = 5

c = C()
c.__dict__["y"] = 10
print(c.__dict__)
# {'x': 5, 'y': 10}
