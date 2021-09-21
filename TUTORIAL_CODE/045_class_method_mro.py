class InputData(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


# Other InputData subclasses could read from the network, decompress data transparently, etc

class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result

import os
from threading import Thread
def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


from tempfile import TemporaryDirectory


def write_test_files(tmpdir):
    pass # ...

with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    result = mapreduce(tmpdir)

print('There are', result, 'lines')

# There are 4360 lines

'''
What’s the problem? The huge issue is the mapreduce function is not generic at all.
If you want to write another InputData or Worker subclass,
you would also have to rewrite the generate_inputs,
create_workers, and mapreduce functions to match.
'''


class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    # ...
    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    # ...
    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    pass # ...

def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    config = {'data_dir': tmpdir}
    result = mapreduce(LineCountWorker, PathInputData, config)

'''
Now you can write other GenericInputData and GenericWorker classes
as you wish and not have to rewrite any of the glue code.

Python only supports a single constructor per class, the __init__ method.
Use @classmethod to define alternative constructors for your classes.
Use class method polymorphism to provide generic ways to build and connect concrete subclasses.
'''


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


class TimesTwo(object):
    def __init__(self):
        self.value *= 2


class PlusFive(object):
    def __init__(self):
        self.value += 5


class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


foo = OneWay(5)
print('First ordering is (5 * 2) + 5 =', foo.value)


# First ordering is (5 * 2) + 5 = 15

class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


bar = AnotherWay(5)
print('Second ordering still is', bar.value)

# Second ordering still is 15

'''
Diamond inheritance happens when a subclass inherits from two separate 
classes that have the same superclass somewhere in the hierarchy. 
Diamond inheritance causes the common superclass’s __init__ method
 to run multiple times, causing unexpected behavior.
'''


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


foo = ThisWay(5)
print('Should be (5 * 5) + 2 = 27 but is', foo.value)

# Should be (5 * 5) + 2 = 27 but is 7

'''
Python 2.2 added the super built-in function and defined the method resolution order (MRO) 
- depth-first, left-to-right
It also ensures that common superclasses in diamond hierarchies are only run once.
'''


# Python 2
class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


# Python 2
class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


foo = GoodWay(5)
print('Should be 5 * (5 + 2) = 35 and is', foo.value)
# Should be 5 * (5 + 2) = 35 and is 35

from pprint import pprint

pprint(GoodWay.mro())

'''
[<class '__main__.GoodWay'>,
<class '__main__.TimesFiveCorrect'>,
<class '__main__.PlusTwoCorrect'>,
<class '__main__.MyBaseClass'>,
<class 'object'>]
'''


# Python 3 fixes these issues by making calls to super with no arguments equivalent to calling super with __class__ and self specified

class Explicit(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value * 2)


class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)


assert Explicit(10).value == Implicit(10).value

# This works because Python 3 lets you reliably reference the current class in methods using the __class__ variable. This doesn’t work in Python 2 because __class__ isn’t defined.
