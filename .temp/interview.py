class C:
    surname = "patankar"

    def __init__(self, name):
        self.name = name

    @classmethod
    def myclassmethod(cls):
        print("start of class method")
        print(f"my class method {cls.surname}")
        print("calling instance method from class method")
        # cls.myinstancemethod()
        print("not possible")
        print("end of class method")

    def myinstancemethod(self):
        print("start of instance method")
        print(f"my instance method {self.name} {self.surname}")
        print("calling class method from instance method")
        self.myclassmethod()
        print("end of instance of method")

c = C("smita")
print("calling class method on instance")
c.myclassmethod()
print("calling instance method on instance")
c.myinstancemethod()

print("\n")

print("calling class method on class")
C.myclassmethod()
print("calling instance method for class")
C.myinstancemethod(c)

# change params of overriden method

# search match

# "smitaneha"
# match

# l = [0,1,2,3,4,5]

# -1:-7:-1

# dict dup

a, b ,c = 1000, 2000, 3000

# args kwargs
