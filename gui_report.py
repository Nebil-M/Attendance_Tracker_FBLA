import customtkinter as ct
from tkinter import ttk
import tkinter as tk
from Report import report_manager, prize_manager
from func_utils import limited_weight_cells, place_holder_bind_all


class ReportController:
    def __init__(self, view):
        self.view = view


class ReportFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ct.CTkLabel(self, text='\nName', font=('arial', 30))
        self.name.grid(row=0, column=0, sticky='NEWS')

        self.display = Display(self)
        self.display.grid(row=1, column=0, sticky='NEWS', padx=20, pady=20)

        self.prize_frame = PrizeFrame(self)
        self.prize_frame.grid(row=1, column=1, sticky='NEWS', padx=20, pady=20, rowspan=2)

        self.report_toggle = ReportToggle(self)
        self.report_toggle.grid(row=2, column=0, sticky='NEWS', padx=20, pady=20)

        limited_weight_cells(self)

        self.manual_weights()

    def manual_weights(self):
        # Table scrolls
        self.prize_frame.prize_table.rowconfigure(2, weight=0)
        self.prize_frame.prize_table.columnconfigure(1, weight=0)

        # Winner Labels
        self.display.winner_display.rowconfigure(0, weight=0)
        self.display.winner_display.rowconfigure(2, weight=0)

        # prizes label and buttons
        self.prize_frame.rowconfigure(0, weight=0)
        self.prize_frame.rowconfigure(3, weight=0)
        self.prize_frame.rowconfigure(4, weight=0)
        self.prize_frame.rowconfigure(5, weight=0)

        # Student list displays
        self.display.student_list.rowconfigure(0, weight=0)

        # Create button
        self.display.rowconfigure(1, weight=0)

        # Toggle
        self.rowconfigure(2, weight=0)

        # Name label
        self.rowconfigure(0, weight=0)


class PrizeFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(border_width=5, border_color='black')
        # Label
        self.label = ct.CTkLabel(self, text='Prizes', font=('arial', 30))
        self.label.grid(row=0, column=0, sticky='NEWS', padx=20, pady=20)
        # Table
        self.prize_table = PrizeTable(self)
        self.prize_table.grid(row=1, column=0, sticky='NEWS', padx=30)

        # Buttons
        font = ('arial', 15)
        corner_radius = 10
        pad_x = 30
        pad_y = 5
        height = 40
        self.add_button = ct.CTkButton(self, text='Add prize', font=font, corner_radius=corner_radius, height=height)
        self.add_button.grid(row=3, column=0, sticky='NEWS', padx=pad_x, pady=pad_y)

        self.delete_button = ct.CTkButton(self, text='Delete prize', font=font, corner_radius=corner_radius,
                                          height=height)
        self.delete_button.grid(row=4, column=0, sticky='NEWS', padx=pad_x, pady=pad_y)

        self.edit_button = ct.CTkButton(self, text='Edit prize', font=font, corner_radius=corner_radius, height=height)
        self.edit_button.grid(row=5, column=0, sticky='NEWS', padx=pad_x, pady=(pad_y, pad_y + 20))


class PrizeTable(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Styling
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', fieldbackground='#343638', rowheight=40)
        s.configure('Treeview.Heading',
                    background="#343638", foreground='gray',
                    font=('Helvetica', 20, 'bold'), fieldbackground='#343638')

        # Initialising and Setting Scroll
        self.tree = ttk.Treeview(self, show='headings')
        self.tree.grid(row=1, column=0, sticky='NEWS')
        self.scroll_y = ct.CTkScrollbar(self, orientation="vertical", command=self.tree.yview)
        self.scroll_y.grid(row=1, column=1, sticky='NEWS')
        self.tree.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_x = ct.CTkScrollbar(self, orientation="horizontal", command=self.tree.xview)
        self.scroll_x.grid(row=2, column=0, sticky='NEWS')
        self.tree.configure(xscrollcommand=self.scroll_x.set)

        # setting up columns
        columns = ("Prize Name", 'Required Points')
        self.tree["columns"] = columns
        for column in columns:
            self.tree.heading(column, text=column)
            if column == 'Required Points':
                self.tree.column(column, width=200, anchor='center', minwidth=250)
            else:
                self.tree.column(column, width=200, anchor='center', minwidth=200)

    def load(self, prizes):
        for prize in prizes:
            values = (prize.name, prize.required_points)
            prize_id = prize.name
            self.tree.insert("", 'end', prize_id, text=prize_id, values=values, tags=('ttk', 'simple'))
            self.tree.tag_configure('ttk', font=('Helvetica', 20, 'bold'), foreground='gray74', background='#343638')


class Display(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.student_list = StudentList(self)
        self.student_list.grid(row=0, column=0, sticky='NEWS', padx=20, pady=10, rowspan=2)

        self.winner_display = WinnersDisplay(self)
        self.winner_display.grid(row=0, column=1, sticky='NEWS', padx=20, pady=10)

        self.create_pdf_button = ct.CTkButton(self, text='Create PDF', height=50, font=('arial', 15))
        self.create_pdf_button.grid(row=1, column=1, sticky='NEWS', padx=40, pady=10)


class StudentList(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = 20
        sticky = 'NEWS'
        pad_x = 0
        pad_y = 0
        self.label_9 = ct.CTkLabel(self, text='Grade Nine', font=('arial', font))
        self.label_9.grid(row=0, column=0, sticky=sticky, padx=pad_x, pady=pad_y)

        self.label_10 = ct.CTkLabel(self, text='Grade Ten', font=('arial', font))
        self.label_10.grid(row=0, column=1, sticky=sticky, padx=pad_x, pady=pad_y)

        self.label_11 = ct.CTkLabel(self, text='Grade Eleven', font=('arial', font))
        self.label_11.grid(row=0, column=2, sticky=sticky, padx=pad_x, pady=pad_y)

        self.label_12 = ct.CTkLabel(self, text='Grade Twelve', font=('arial', font))
        self.label_12.grid(row=0, column=3, sticky=sticky, padx=pad_x, pady=pad_y)

        self.ninth_grade = self.student_list = tk.Listbox(self, height=3, borderwidth=10,
                                                          width=15, background="#343638", activestyle='dotbox',
                                                          font=("Helvetica", 15, "bold"), foreground="gray"
                                                          )
        self.ninth_grade.grid(row=1, column=0, sticky='NEWS')

        self.eleventh_grade = self.student_list = tk.Listbox(self, height=3, borderwidth=10,
                                                             width=15, background="#343638", activestyle='dotbox',
                                                             font=("Helvetica", 15, "bold"), foreground="gray"
                                                             )
        self.eleventh_grade.grid(row=1, column=1, sticky='NEWS')

        self.tenth_grade = self.student_list = tk.Listbox(self, height=3, borderwidth=10,
                                                          width=15, background="#343638", activestyle='dotbox',
                                                          font=("Helvetica", 15, "bold"), foreground="gray"
                                                          )
        self.tenth_grade.grid(row=1, column=2, sticky='NEWS')

        self.twelfth_grade = self.student_list = tk.Listbox(self, height=3, borderwidth=10,
                                                            width=15, background="#343638", activestyle='dotbox',
                                                            font=("Helvetica", 15, "bold"), foreground="gray"
                                                            )
        self.twelfth_grade.grid(row=1, column=3, sticky='NEWS')

        # adding the variables
        self.add_vars()

    def add_vars(self):
        self.ninth_grade.var = tk.StringVar(value=[])
        self.ninth_grade.configure(listvariable=self.ninth_grade.var)
        self.tenth_grade.var = tk.StringVar(value=[])
        self.tenth_grade.configure(listvariable=self.ninth_grade.var)
        self.eleventh_grade.var = tk.StringVar(value=[])
        self.eleventh_grade.configure(listvariable=self.ninth_grade.var)
        self.twelfth_grade.var = tk.StringVar(value=[])
        self.twelfth_grade.configure(listvariable=self.ninth_grade.var)


class WinnersDisplay(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = 20
        sticky = 'NEWS'
        pad_x = 0
        pad_y = 0

        ct.CTkLabel(self, text='Top winner', font=('arial', font)).grid(row=0, column=0, sticky=sticky, padx=pad_x,
                                                                        pady=pad_y)
        self.top_winner = ct.CTkTextbox(self)
        self.top_winner.grid(row=1, column=0, sticky='NEWS', padx=10, pady=10)

        ct.CTkLabel(self, text='Random winners', font=('arial', font)).grid(row=2, column=0, sticky=sticky, padx=pad_x,
                                                                            pady=pad_y)
        self.random_winner = ct.CTkTextbox(self)
        self.random_winner.grid(row=3, column=0, sticky='NEWS', padx=10, pady=10)


class ReportToggle(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.left_toggle = ct.CTkButton(self, text='←', font=('arial', 30), height=20, corner_radius=0)
        self.left_toggle.grid(row=0, column=0, sticky="NEWS", padx=30, pady=10)

        self.end_quarter = ct.CTkButton(self, text='Click to end quarter', font=('arial', 30), height=50,
                                        corner_radius=10)
        self.end_quarter.grid(row=0, column=1, sticky="NEWS", padx=30, pady=10)

        self.right_toggle = ct.CTkButton(self, text='→', font=('arial', 30), height=20, corner_radius=0)
        self.right_toggle.grid(row=0, column=2, sticky="NEWS", padx=30, pady=10)


if __name__ == '__main__':
    ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ct.set_default_color_theme("dark-blue")
    root = ct.CTk()
    # root.geometry("500x500")

    w = ReportFrame(root)
    w.grid(row=0, column=0, sticky='NEWS')
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
