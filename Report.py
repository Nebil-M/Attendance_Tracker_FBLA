import pickle
from student import student_manager
import copy


class Prize:
    def __init__(self, name, required_points: int):
        self.name = name
        self.required_points = required_points

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"Prize('{self.name}', {self.required_points})"


class PrizeManager:
    def __init__(self):
        self.prizes = []
        self.load_data()

    def add_prize(self, name, required_points):
        self.prizes.append(Prize(name, required_points))

    def delete_prize(self, prize):
        self.prizes.remove(prize)

    def get_prize(self, name):
        for prize in self.prizes:
            if prize.name == name:
                return prize

    def load_data(self, file_name='prizes'):
        with open(f'project_data/Report/Prizes/{file_name}.pkl', 'rb') as data_input:
            self.prizes = pickle.load(data_input)

    def save_data(self, file_name='prizes'):
        with open(f'project_data/Report/Prizes/{file_name}.pkl', 'wb') as data_output:
            pickle.dump(self.prizes, data_output, pickle.HIGHEST_PROTOCOL)

    def award_prize(self, student):
        if student is None:
            return "No winners from this grade"
        possible_prizes = [prize for prize in self.prizes if prize.required_points <= student.points]
        best_possible_prize = max(possible_prizes, key=lambda prize: prize.required_points)
        return best_possible_prize


class Report:
    def __init__(self, name: str = "NoName"):

        self.name = name

        self.random_winners = list(map(copy.copy, student_manager.get_random_winners()))
        self.top_winner = copy.copy(student_manager.get_winner())
        self.winners = self.random_winners + [self.top_winner, ]

        self.ninth_graders = list(map(copy.copy, student_manager.get_grade_students(9)))
        self.tenth_graders = list(map(copy.copy, student_manager.get_grade_students(10)))
        self.eleventh_graders = list(map(copy.copy, student_manager.get_grade_students(11)))
        self.twelfth_graders = list(map(copy.copy, student_manager.get_grade_students(12)))

        self.students_with_prize = [(copy.copy(student), copy.copy(prize_manager.award_prize(student)))
                                    for student in self.winners]

    def __repr__(self):
        return f'Report: {self.name}'

    def __str__(self):
        return f'A Report Object with the following name: {self.name}'


class ReportManager:
    def __init__(self):
        self.reports = []
        #self.load_data()
        self.idx = 0

    def create_report(self, name: str = "NoName"):
        report = Report(name)
        self.reports.insert(0, report)
        return report

    def current(self):
        reports = [self.reports.index(report) for report in self.reports]
        if self.idx in reports:
            return self.reports[self.idx]

    def next(self):
        reports = [self.reports.index(report) for report in self.reports]
        if self.idx + 1 in reports:
            self.idx += 1
            return self.current()

    def prev(self):
        reports = [self.reports.index(report) for report in self.reports]
        if self.idx - 1 in reports:
            self.idx -= 1
            return self.current()

    def load_data(self, file_name='Report'):
        with open(f'project_data/Report/Reports/{file_name}.pkl', 'rb') as data_input:
            self.reports = pickle.load(data_input)

    def save_data(self, file_name='Report'):
        with open(f'project_data/Report/Reports/{file_name}.pkl', 'wb') as data_output:
            pickle.dump(self.reports, data_output, pickle.HIGHEST_PROTOCOL)


prize_manager = PrizeManager()
report_manager = ReportManager()
