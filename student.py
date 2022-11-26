import pickle
import random


class Student:
    def __init__(self, name: str, grades: str, grade_level: int, points: int = 0):
        self.name = name
        self.grades = grades
        self.grade_level = grade_level
        self.points = points

    def add_points(self, n=1):
        self.points += n

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Student({self.name}, {self.grades}, {self.grade_level}, {self.points})"


class StudentManager:
    def __init__(self):
        self.students = []
        self.prizes = {"150$ gift card": 50, '100$ gift card': 30, 'Pizza': 25, 'Edison Shirt': 15, 'Donut': 10,
                       'Candy': 8, 'Edison sticker': 5, 'Pencil': 1}
        self.load_data()

    def add_student(self, name, grades, grade_level, points=0):
        self.students.append(Student(name, grades, grade_level, points))

    def remove_student(self, remove_student):
        self.students = [student for student in self.students if student != remove_student]

    def get_student(self, name):
        for student in self.students:
            if name == student.name:
                return student

    def reset_points(self):
        for student in self.students:
            student.points = 0

    def get_winner(self):
        students_with_most_points = max(self.students, key=lambda student: student.points)
        return students_with_most_points

    def get_random_winners(self):
        grade_9_students = [student for student in self.students if student.grade_level == 9 and student.points != 0]
        grade_10_students = [student for student in self.students if student.grade_level == 10 and student.points != 0]
        grade_11_students = [student for student in self.students if student.grade_level == 11 and student.points != 0]
        grade_12_students = [student for student in self.students if student.grade_level == 12 and student.points != 0]

        grade_9_winner = random.choice(grade_9_students) if grade_9_students else None
        grade_10_winner = random.choice(grade_10_students) if grade_10_students else None
        grade_11_winner = random.choice(grade_11_students) if grade_11_students else None
        grade_12_winner = random.choice(grade_12_students) if grade_12_students else None

        return grade_9_winner, grade_10_winner, grade_11_winner, grade_12_winner

    def get_prize(self, student):
        if student is None:
            return "No winners from this grade"
        possible_prizes = {prize: self.prizes[prize] for prize in self.prizes if self.prizes[prize] <= student.points}
        best_possible_prize = max(possible_prizes, key=possible_prizes.get)
        return best_possible_prize

    def load_data(self, file_name='students'):
        with open(f'project_data/students/{file_name}.pkl', 'rb') as data_input:
            self.students = pickle.load(data_input)

    def save_data(self, file_name='students'):
        with open(f'project_data/students/{file_name}.pkl', 'wb') as data_output:
            pickle.dump(self.students, data_output, pickle.HIGHEST_PROTOCOL)

    def end_quarter(self):
        ...

    def generate_report(self):
        ...
