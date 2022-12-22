import pickle
import random


class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, letter_grade: str, grade_level: int, points: int = 0):
        self.letter_grade_options = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]

        # data validation for the parameters :)
        if student_id < 58010000 or student_id > 58019999:
            raise ValueError("Parameter student_id must be an integer between 58010000 and 58019999.")
        if grade_level < 9 or grade_level > 12:
            raise ValueError("Parameter grade_level must be an integer between 9 and 12.")
        if letter_grade not in self.letter_grade_options:
            raise ValueError(f"Parameter letter_grade is not one of the following values: {self.letter_grade_options}")
        if points < 0:
            raise ValueError("Parameter points should not be less than zero.")

        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.letter_grade = letter_grade
        self.grade_level = grade_level
        self.points = points

    def add_points(self, n=1):
        self.points += n

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Student({self.student_id}, {self.first_name}, {self.last_name}, {self.letter_grade}, {self.grade_level}, {self.points})"


class StudentManager:
    def __init__(self):
        self.students = []
        self.prizes = {"150$ gift card": 50, '100$ gift card': 30, 'Pizza': 25, 'Edison Shirt': 15, 'Donut': 10,
                       'Candy': 8, 'Edison sticker': 5, 'Pencil': 1}
        self.load_data()

    def add_student(self, student_id, first_name, last_name, letter_grade, grade_level, points=0):
        self.students.append(Student(student_id, first_name, last_name, letter_grade, grade_level, points))

    # This allows you to edit a student's details. The edit_attribute is the thing that you want to edit, like first_name, last_name, etc.
    def edit_student(self, student_id, edit_attribute: str, new_value):
        student = self.get_student(student_id)
        possible_attributes = ["student_id", "first_name", "last_name", "letter_grade", "grade_level", "points"]

        # Checks if the edit_attribute is one of the attributes that can be edited.
        if edit_attribute not in possible_attributes:
            raise ValueError(f"edit_attribute should be one of the following: {possible_attributes}")

        # Changes the details of the student
        # i hope there's an easier way to do this.
        # Also just a note, there's no data validation here. we should add that at some point.
        if edit_attribute == possible_attributes[0]:
            student.student_id = new_value
        elif edit_attribute == possible_attributes[1]:
            student.first_name = new_value
        elif edit_attribute == possible_attributes[2]:
            student.last_name = new_value
        elif edit_attribute == possible_attributes[3]:
            student.letter_grade = new_value

        # Removes the old student with its old details
        self.remove_student(student_id)

        # Adds the new student with its updated details
        self.add_student(student.student_id, student.first_name, student.last_name, student.letter_grade, student.grade_level, student.points)

        return student

    def remove_student(self, student_id):
        try:
            self.students.remove(self.get_student(student_id))
        except ValueError:
            print("ValueError with the remove method in student.py StudentManager class")

    def get_student(self, student_id):
        for student in self.students:
            if student_id == student.student_id:
                return student

    def reset_points(self):
        for student in self.students:
            student.points = 0

    # Student With top points
    def get_winner(self):
        student_with_most_points = max(self.students, key=lambda student: student.points)
        return student_with_most_points

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
