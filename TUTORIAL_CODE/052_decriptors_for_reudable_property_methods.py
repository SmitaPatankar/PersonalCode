class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value

galileo = Homework()
galileo.grade = 95

class Exam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value

# tedious above
# For this purpose, descriptors are also better than mix-ins

class Grade(object):
    def __get__(*args, **kwargs):
        pass  # ...

    def __set__(*args, **kwargs):
        pass  # ...

class Exam(object):
    # Class attributes
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()

exam = Exam()
exam.writing_grade = 40

# backend
# Exam.__dict__['writing_grade'].__set__(exam, 40)

print(exam.writing_grade)

# backend
print(Exam.__dict__['writing_grade'].__get__(exam, Exam))

class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value

first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 99
print('Writing', first_exam.writing_grade)
print('Science', first_exam.science_grade)

'''
Writing 82
Science 99
'''

second_exam = Exam()
second_exam.writing_grade = 75
print('Second', second_exam.writing_grade, 'is right')
print('First ', first_exam.writing_grade, 'is wrong')

'''
Second 75 is right
First  75 is wrong
'''

# The Grade instance for this attribute is constructed once in the program
# lifetime when the Exam class is first defined,
# not each time an Exam instance is created.

class Grade(object):
    def __init__(self):
        self._values = {}

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value

# This causes instances to never have their reference count go to zero,
# preventing cleanup by the garbage collector.

from weakref import WeakKeyDictionary
class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()
    pass  # ...

class Exam(object):
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()
first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
print('First ', first_exam.writing_grade, 'is right')
print('Second', second_exam.writing_grade, 'is right')

'''
First  82 is right
Second 75 is right
'''
