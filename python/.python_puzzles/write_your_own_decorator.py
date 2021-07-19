def retry(somemainfunction):
    def newfunction(*args, **kwargs):
        i = 0
        for i in range(3):
            try:
                return somemainfunction(*args, **kwargs)
            except ZeroDivisionError:
                if i == 2:
                    raise ZeroDivisionError
                else:
                    print("retrying")
    return newfunction

@retry
def mainfunction(a, b):
    return a//b

print(mainfunction(10,2))
