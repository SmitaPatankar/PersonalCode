def trycatch(f):
    def newf(a, b):
        try:
            f(a, b)
        except:
            print("issue")
    return newf

@trycatch
def div(a,b):
    return a/b

print(div(10,0))
