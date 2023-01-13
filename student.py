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

    def add_student(self, student_id: int, first_name: str, last_name: str, letter_grade: str, grade_level: int,
                    points=0):
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

        # Returns none if the ID is not in the database
        return None

    def reset_points(self):
        for student in self.students:
            student.points = 0

    def get_grade_students(self, grade_level: int):
        students = filter(lambda student: student.grade_level == grade_level, self.students)
        sorted_students = list(sorted(students, key=lambda student: student.points))
        return sorted_students

    def get_winner(self):
        student_with_most_points = max(self.students, key=lambda student: student.points)
        return student_with_most_points

    def get_random_winners(self, exclude=[]):
        grade_9_students = [student for student in self.get_grade_students(9) if student.student_id not in exclude]
        grade_10_students = [student for student in self.get_grade_students(10) if student.student_id not in exclude]
        grade_11_students = [student for student in self.get_grade_students(11) if student.student_id not in exclude]
        grade_12_students = [student for student in self.get_grade_students(12) if student.student_id not in exclude]

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

    def validate_id(self, student_id: str, student=None):
        if student_id == "Student ID" or student_id == "":
            return "\tThe Student ID must be filled out."

        try:
            student_id = int(student_id)
        except ValueError:
            return "\tThe Student ID may only include whole numbers."

        ids = [student.student_id for student in self.students]
        if student_id < 58010000 or student_id > 58019999:
            return "\tThe Student ID must be an 8 digit number starting with 5801."
        elif student:
            other_students_id = [s.student_id for s in self.students if s.student_id != student.student_id]
            if student_id in other_students_id:
                return "\tThis Student ID is already assigned to another student."
        elif student_id in ids:
            return "\tThis Student ID is already assigned to another student."

        # If none of the other return statements are triggered, return True (meaning it passed the tests.)
        return True

    def validate_first_name(self, first_name):
        if first_name == "First name" or first_name == "":
            return "\tThe student's first name must be filled out."

        # Gets rid of spaces and hyphens, which means the name may have spaces or hyphens.
        first_name = first_name.replace(' ', '').replace('-', '')
        if not first_name.isalpha():
            return "\tThe student's first name may only include letters, hyphens, and spaces."

        # If none of the other return statements are triggered, return True (meaning it passed the tests.)
        return True

    def validate_last_name(self, last_name):
        if last_name == "Last name" or last_name == "":
            return "\tThe student's last name must be filled out."

        # Gets rid of spaces and hyphens, which means the name may have spaces or hyphens.
        last_name = last_name.replace(' ', '').replace('-', '')

        if not last_name.isalpha():
            return "\tThe student's last name may only include letters, hyphens, and spaces."

        # If none of the other return statements are triggered, return True (meaning it passed the tests.)
        return True

    def validate_grade_level(self, grade_level: str):
        grade_level_options = ['9', '10', '11', '12']

        if grade_level not in grade_level_options:
            return "\tA grade level must be selected."

        # If none of the other return statements are triggered, return True (meaning it passed the tests.)
        return True

    def validate_letter_grade(self, letter_grade):
        # No A+ in the options, because our school district does not have A+ available.
        letter_grade_options = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]

        if letter_grade not in letter_grade_options:
            return "\tA letter grade must be selected."

        # If none of the other return statements are triggered, return True (meaning it passed the tests.)
        return True


student_manager = StudentManager()
