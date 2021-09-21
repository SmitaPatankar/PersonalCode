class SimpleGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)

book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)
print(book.average_grade('Isaac Newton'))  # 90.0

class BySubjectGradebook(object):
    def __init__(self):
        self._grades = {}
    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)

class WeightedGradebook(object):
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject.setdefault(subject, [])
        grade_list.append((score, weight))

    def average_grade(self, name):
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                pass # ...
        return score_sum / score_count

book.report_grade('Albert Einstein', 'Math', 80, 0.10)

# avoid dictionaries that contain dictionaries

# (score, weight)
# grades = []
# grades.append((95, 0.45))
# ...
# total = sum(score * weight for score, weight in grades)
# total_weight = sum(weight for _, weight in grades)
# average_grade = total / total_weight

# _ (the underscore variable name, a Python convention for unused variables)
# grades = []
# grades.append((95, 0.45, 'Great job'))
# ...
# total = sum(score * weight for score, weight, _ in grades)
# total_weight = sum(weight for _, weight, _ in grades)
# average_grade = total / total_weight


import collections
Grade = collections.namedtuple('Grade', ('score', 'weight'))
