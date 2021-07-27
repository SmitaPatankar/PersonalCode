# # we can call instance method on instance
# # we can call instance method on class if we pass instance as a parameter
# # we cannot call instance method inside class method because we dont know which instance it is for

# class C:
#     surname = "patankar"

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def myclassmethod(cls):
#         print("start of class method")
#         print(f"my class method {cls.surname}")
#         print("calling instance method from class method")
#         cls.myinstancemethod()
#         print("not possible")
#         print("end of class method")

#     def myinstancemethod(self):
#         print("start of instance method")
#         print(f"my instance method {self.name} {self.surname}")
#         print("calling class method from instance method")
#         self.myclassmethod()
#         print("end of instance of method")

# c = C("smita")
# print("calling class method on instance")
# c.myclassmethod()
# print("calling instance method on instance")
# c.myinstancemethod()

# print("\n")

# print("calling class method on class")
# C.myclassmethod()
# print("calling instance method on class")
# C.myinstancemethod(c)

s = zip([1,2,3],[4,5])
print(dict(s))


# shift left in devops
# take input for bash script9t
# pod
# replica
# hor ver
# lambda
