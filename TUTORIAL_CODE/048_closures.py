''''
closures can access local variables of its outer function
'''

# class

class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

avg = Averager()

avg(10)
# 10.0
avg(11)
# 10.5
avg(12)
# 11.0


# high order function

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

avg = make_averager()
avg(10)
# 10.0
avg(11)
# 10.5
avg(12)
# 11.0

avg.__code__.co_varnames
# ('new_value', 'total')
avg.__code__.co_freevars
# ('series',)

avg.__code__.co_freevars
# ('series',)
avg.__closure__
# (<cell at 0x107a44f78: list object at 0x107a91a48>,)
avg.__closure__[0].cell_contents
# [10, 11, 12]

