import customtkinter as ct
from tkinter import ttk
import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from student import student_manager
from Events import event_manager
from Report import report_manager, prize_manager
from func_utils import limited_weight_cells, place_holder_bind_all, place_holder_bind_widget


class HomeController:
    def __init__(self, view):
        self.view = view
        # vars
        self.number_frame = self.view.number_frame
        self.points_frame = self.view.points_frame
        self.graph = self.view.graph

        # Initial funcs
        self.update()

    def update_graph(self):
        grades = [9, 10, 11, 12]
        points_per_grade = [sum([student.points for student in student_manager.get_grade_students(grade)]) for grade in grades]
        self.graph.load_graph(points_per_grade)

    def update_text(self):
        grade_9 = len(student_manager.get_grade_students(9))
        grade_10 = len(student_manager.get_grade_students(10))
        grade_11 = len(student_manager.get_grade_students(11))
        grade_12 = len(student_manager.get_grade_students(12))

        sport_events = len(event_manager.get_sport_events())
        non_sport_events = len(event_manager.get_non_sport_events())

        total_points = sum(student.points for student in student_manager.students)

        self.number_frame.students_number.configure(text=
                    f'''9th Grade: {grade_9}\n10th Grade: {grade_10}\n11th Grade: {grade_11}\n12th Grade: {grade_12}''')
        self.number_frame.events_number.configure(text=
                                                f'Sport Events: {sport_events}\nNon-Sport Events: {non_sport_events}\n')
        self.points_frame.points_number.configure(text=f'{total_points}')

    def update(self):
        self.update_graph()
        self.update_text()





class HomeFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = ct.CTkLabel(self, text='Attendance Tracker', font=('arial', 40, "bold", 'italic'))
        label.grid(row=0, column=0, sticky='NEWS', padx=10, pady=20, columnspan=2)
        self.graph = Graph(self, width=400)
        self.graph.grid(row=1, column=0, sticky='NEWS', padx=10, pady=20, rowspan=2)
        self.number_frame = NumberFrame(self)
        self.number_frame.grid(row=1, column=1, sticky='NEWS', padx=10, pady=20)

        self.points_frame = PointsFrame(self)
        self.points_frame.grid(row=2, column=1, sticky='NEWS', padx=10, pady=20)

        limited_weight_cells(self)


class Graph(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(border_width=10)

        fig = Figure()
        self.ax = fig.add_subplot()
        self.x = ['9th Grade', '10th Grade', '11th Grade', '12th Grade']
        self.y = [3, 4, 5, 6]
        self.bar = self.ax.bar(self.x, self.y, width=1, edgecolor="white", linewidth=0.7)
        self.ax.set_xlabel("Grade Level")
        self.ax.set_ylabel("Total Points in Grade")

        self.plot_canvas = FigureCanvasTkAgg(fig, master=self)
        self.plot_canvas.draw()
        self.plot_canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)

    def load_graph(self, y):
        self.y = y
        self.bar.remove()
        self.bar = self.ax.bar(self.x, self.y, width=1, edgecolor="white", linewidth=0.7, color='lightblue')
        self.plot_canvas.draw()




class NumberFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        student_label = ct.CTkLabel(self, text='\tNumber of Students:\t ', font=('arial', 20, 'bold'))
        student_label.grid(row=0, column=0, sticky='NEWS', padx=5, pady=10)
        self.students_number = ct.CTkLabel(self, text='9th Grade:\n10th Grade:\n11th Grade:\n12th Grade:',
                                           font=('arial', 15, 'bold'), anchor='w')
        self.students_number.grid(row=1, column=0, sticky='NEWS', padx=5, pady=0)

        event_label = ct.CTkLabel(self, text='Number of Events:\t ', font=('arial', 20, 'bold'))
        event_label.grid(row=2, column=0, sticky='NEWS', padx=5, pady=10)
        self.events_number = ct.CTkLabel(self, text='Sport Events:\nNon-Sport Events:\n',
                                         font=('arial', 15, 'bold'), anchor='w')
        self.events_number.grid(row=3, column=0, sticky='NEWS', padx=5, pady=0)


class PointsFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        points_label = ct.CTkLabel(self, text='\nTotal points:', font=('arial', 20, 'bold'))
        points_label.grid(row=0, column=0, sticky='NEWS', padx=5, pady=10)
        self.points_number = ct.CTkLabel(self, text='0\n', font=('arial', 25, 'bold'))
        self.points_number.grid(row=1, column=0, sticky='NEWS', padx=5, pady=0)


if __name__ == '__main__':
    ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ct.set_default_color_theme("dark-blue")
    root = ct.CTk()

    w = HomeFrame(root)
    HC = HomeController(w)
    w.grid(row=0, column=0, sticky='NEWS')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
