import customtkinter as ct
from tkinter import ttk
import tkinter as tk
from student import student_manager
from Events import event_manager
from Report import report_manager, prize_manager
from func_utils import limited_weight_cells, place_holder_bind_all, place_holder_bind_widget


class HomeFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = ct.CTkLabel(self, text='Attendance Tracker', font=('arial', 40, "bold", 'italic'))
        label.grid(row=0, column=0, sticky='NEWS', padx=10, pady=20, columnspan=2)
        graph = Graph(self, width=400)
        graph.grid(row=1, column=0, sticky='NEWS', padx=10, pady=20, rowspan=2)
        number_frame = NumberFrame(self)
        number_frame.grid(row=1, column=1, sticky='NEWS', padx=10, pady=20)

        points_frame = PointsFrame(self)
        points_frame.grid(row=2, column=1, sticky='NEWS', padx=10, pady=20)

        limited_weight_cells(self)


class Graph(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


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
    w.grid(row=0, column=0, sticky='NEWS')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
