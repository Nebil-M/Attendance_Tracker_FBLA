import random
import pickle

class Student:
    def __init__(self, name, grades, grade_level, points=0):
        self.name = name
        self.grades = grades
        self.grade_level = grade_level
        self.points = points

    def add_point(self, n=1):
        self.points += n

    def present(self, name, grades, grade_level, points):
        ...


class Students:
    def __init__(self):
        self.students = []

    def add_student(self, name, grades, grade_level, points=0):
        self.students.append(Student(name, grades, grade_level, points))

    def remove_student(self):
        ...

    def get_winners(self):
        ...

    def get_random_winner(self):
        return random.choice(self.students)

    def get_prize(self, student):
        ...

    def load_data(self):
        ...

    def save_data(self):
        ...

    def generate_report(self):
        ...
