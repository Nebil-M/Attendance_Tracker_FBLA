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
        self.popular_frame = self.view.popular_frame
        self.points_frame = self.view.points_frame
        self.graph = self.view.graph

        # Initial funcs
        self.update()

    def update_graph(self):
        grades = [9, 10, 11, 12]
        points_per_grade = [sum([student.points for student in student_manager.get_grade_students(grade)]) for grade in
                            grades]
        self.graph.load_graph(points_per_grade)

    def update_text(self):
        unsorted_events = [event for event in event_manager.events]
        events = sorted(unsorted_events, key=lambda e: len(e.attendees), reverse=True)
        number_of_events = len(event_manager.events)
        if number_of_events > 3:
            most_popular_events = events[:3]
        else:
            most_popular_events = events[:number_of_events]
        popular_events_str = ''.join([f'{event.name}:   {len(event.attendees)}  attendees\n'
                                      for event in most_popular_events])
        self.popular_frame.popular_events.configure(text=popular_events_str, justify=tk.LEFT)

        total_points = sum(student.points for student in student_manager.students)
        self.points_frame.points_number.configure(text=f'{total_points}')

    def update(self):
        self.update_graph()
        self.update_text()


class HomeFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = ct.CTkLabel(self, text='Attendance Tracker', font=('arial', 60, "bold"))
        label.grid(row=0, column=0, sticky='NEWS', padx=10, pady=20, columnspan=2)
        self.graph = Graph(self, width=400)
        self.graph.grid(row=1, column=0, sticky='NEWS', padx=10, pady=20, rowspan=2)
        self.popular_frame = PopularFrame(self)
        self.popular_frame.grid(row=1, column=1, sticky='NEWS', padx=10, pady=20)

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
        self.plot_canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky='NEWS')

    def load_graph(self, y):
        self.y = y
        self.bar.remove()
        self.bar = self.ax.bar(self.x, self.y, width=1, edgecolor="white", linewidth=0.7, color='lightblue')
        self.plot_canvas.draw()


class PopularFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        popular_label = ct.CTkLabel(self, text=' Most popular Events: ', font=('arial', 40, 'bold', 'italic'))
        popular_label.grid(row=0, column=0, sticky='NEWS', padx=5, pady=10)
        self.popular_events = ct.CTkLabel(self, text='', font=('arial', 20, 'bold'), anchor='n')
        self.popular_events.grid(row=1, column=0, sticky='NEWS', padx=5, pady=0)


class PointsFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        points_label = ct.CTkLabel(self, text='\nTotal points:', font=('arial', 20, 'bold', 'italic'))
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
