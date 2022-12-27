import pickle
import random


class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, letter_grade: str, grade_level: int,
                 points: int = 0):
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

    def add_student(self, student_id: int, first_name: str, last_name: str, letter_grade: str, grade_level:int, points=0):
        self.students.append(Student(student_id, first_name, last_name, letter_grade, grade_level, points))

    def remove_student(self, student_id: int):
        try:
            self.students.remove(self.get_student(student_id))
        except ValueError:
            print(f"The student_id {student_id} does not match anyone.")

    def get_student(self, student_id: int):
        for student in self.students:
            # Checks if the programmer made a mistake, accidentally making student.student_id a string.
            if isinstance(student.student_id, str):
                raise ValueError("student.student_id should not be a string.")

            # Returns the student if the ID matches
            if student_id == student.student_id:
                return student

        raise Exception(f"The student ID {student_id} {type(student_id)} does not match any of the students. ")

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


student_manager = StudentManager()
