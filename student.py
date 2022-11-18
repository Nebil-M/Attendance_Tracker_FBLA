import pickle
import random

class Student:
    def __init__(self, name, grades, grade_level, points=0):
        self.name = name
        self.grades = grades
        self.grade_level = grade_level
        self.points = points

    def add_point(self, n=1):
        self.points += n

    def present(self):
        ...


class Students:
    def __init__(self):
        self.students = []

    def add_student(self, name, grades, grade_level, points=0):
        self.students.append(Student(name, grades, grade_level, points))

    def remove_student(self, name):
        self.students = [student for student in self.students if student.name != name]

    def get_winners(self):
        ...

    def get_random_winner(self):
        return random.choice(self.students)

    def get_prize(self, student):
        ...

    def load_data(self):
        with open('project_data/students', 'rb') as data_input:
            self.students = pickle.load(data_input)


    def save_data(self):
        with open('project_data/students', 'wb') as data_output:
            pickle.dump(self.students, data_output, pickle.HIGHEST_PROTOCOL)

    def generate_report(self):
        ...
