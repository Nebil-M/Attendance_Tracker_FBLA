import customtkinter as ct
from tkinter import ttk
import tkinter as tk
from student import student_manager
from Events import event_manager
from Report import report_manager, prize_manager
from func_utils import limited_weight_cells


class ReportController:
    def __init__(self, view):
        # view = ReportFrame(root)
        self.view = view

        # Vars
        self.prize_frame = self.view.prize_frame
        self.table = self.view.prize_frame.prize_table
        self.display = self.view.display
        self.student_list = self.display.student_list
        self.winner_display = self.display.winner_display

        # Initial function
        self.update_table()
        self.update_display()
        self.bindings()

    # Prize mechanics
    def add_prize(self):
        dialog_name = ct.CTkInputDialog(text="Name of Prize: ", title="Add a prize")
        name = dialog_name.get_input()
        if name:
            while not name.isalpha():
                dialog_name = ct.CTkInputDialog(text="The Name may only include letters and spaces.\n\nName of Prize: ",
                                                title="Add a prize", entry_border_color='red')
                name = dialog_name.get_input()

            dialog_points = ct.CTkInputDialog(text="Number of points required to get this prize: ", title="Add a prize")
            points = dialog_points.get_input()
            if points:
                while not points.isdigit():
                    dialog_points = ct.CTkInputDialog(text="Points may only include whole numbers.\n\nPoints required: "
                                                      , title="Add a prize",
                                                      entry_border_color='red')
                    points = dialog_points.get_input()

                prize_manager.add_prize(name, int(points))
                self.update_table()

    def delete_prize(self):
        selected = self.table.tree.selection()
        if selected:
            confirmation = tk.messagebox.askokcancel("Delete report?",
                                                     message="Are you sure you want to delete the selected prize?")
            if confirmation:
                for prize in selected:
                    prize_obj = prize_manager.get_prize(prize)
                    prize_manager.delete_prize(prize_obj)
            self.update_table()
        else:
            self.show_error(['\tNo Prize is selected.'])

    def edit_prize(self):
        self.table.tree.configure(selectmode='browse')
        selected = self.table.tree.focus()
        if selected:
            name = self.prize_frame.name_entry.get()
            points = self.prize_frame.points_entry.get()
            prize = prize_manager.get_prize(selected)
            errors = []
            valid_name = name.replace('$', '')
            if not valid_name.replace(' ', '').isalnum():
                errors.append('\tThe name may only include letters spaces and numbers.')
            else:
                prize.name = name
            if not points.isdigit():
                errors.append("\tRequired points may only include whole numbers.")
            else:
                prize.required_points = int(points)  # not updating in tree, fix
            self.show_error(errors) if errors else None
            self.update_table()
        else:
            self.show_error(['\tNo Prize is selected.'])


    def fill_edit_field(self):
        prize_name = self.table.tree.focus()
        prize = prize_manager.get_prize(prize_name)

        self.prize_frame.name_entry.delete('0', 'end')
        self.prize_frame.name_entry.insert('end', prize.name)

        self.prize_frame.points_entry.delete('0', 'end')
        self.prize_frame.points_entry.insert('end', prize.required_points)

    def right_arrow(self):
        report_manager.prev()
        self.update_display()

    def left_arrow(self):
        report_manager.next()
        self.update_display()

    def end_quarter(self):
        dialog = ct.CTkInputDialog(text="Name of report: ", title="New report")
        quarter_name = dialog.get_input()
        if quarter_name:
            report_manager.create_report(quarter_name)
            report_manager.idx = 0
            self.update_display()

            # clear Points
            for student in student_manager.students:
                student.points = 0

    def create_pdf_report(self):
        report_manager.idx = 0
        self.update_display()

    def delete_report(self):
        current_report = report_manager.current()
        if current_report:
            confirmation = tk.messagebox.askokcancel("Delete report?",
                                                     message="Are you sure you want to delete the current report?")
            if confirmation:
                report_manager.reports.remove(current_report)
                report_manager.prev()
                self.update_display()

    # Update Events
    def update_table(self):
        self.table.tree.delete(*self.table.tree.get_children())
        self.table.load(prize_manager.prizes)

    def update_display(self):
        # points per student
        current_report = report_manager.current()
        if current_report:
            name_point_9 = [f'{student.first_name} {student.last_name}: {student.points}' for student in
                            current_report.ninth_graders]
            name_point_10 = [f'{student.first_name} {student.last_name}: {student.points}' for student in
                             current_report.tenth_graders]
            name_point_11 = [f'{student.first_name} {student.last_name}: {student.points}' for student in
                             current_report.eleventh_graders]
            name_point_12 = [f'{student.first_name} {student.last_name}: {student.points}' for student in
                             current_report.twelfth_graders]
            self.student_list.ninth_grade.var.set(name_point_9)
            self.student_list.tenth_grade.var.set(name_point_10)
            self.student_list.eleventh_grade.var.set(name_point_11)
            self.student_list.twelfth_grade.var.set(name_point_12)

            self.view.name.configure(text='\n' + current_report.name)
            self.view.date.configure(text='\nDate: ' + current_report.date)
            # winners
            top_winner = current_report.top_winner
            top_winner_string = f'{top_winner.first_name} {top_winner.last_name}:   {prize_manager.award_prize(top_winner)}'
            self.display.winner_display.top_winner.configure(state='normal')
            self.display.winner_display.top_winner.delete("0.0", 'end')
            self.display.winner_display.top_winner.insert('0.0', top_winner_string)
            self.display.winner_display.top_winner.configure(state='disabled')
            # random winners
            random_winners = current_report.random_winners
            if random_winners:
                random_winners_list = [
                    (f'{student.first_name} {student.last_name}:', prize_manager.award_prize(student).name)
                    for student in random_winners if student]
                random_winners_string = ''
                longest = max(random_winners_list, key=lambda st: len(st[0]))
                for s in random_winners_list:
                    l = len(longest[0])
                    m = l - len(s[0])
                    sp = l + m
                    white_s = (' ' * (sp - 12))
                    random_winners_string += s[0] + white_s + s[1] + '\n'
                self.display.winner_display.random_winners.configure(state='normal')
                self.display.winner_display.random_winners.delete("0.0", 'end')
                self.display.winner_display.random_winners.insert('0.0', random_winners_string)
                self.display.winner_display.random_winners.configure(state='disabled')
        else:
            self.view.name.configure(text='\nName')
            self.view.date.configure(text='\nDate')

            self.display.winner_display.top_winner.configure(state='normal')
            self.display.winner_display.top_winner.delete("0.0", 'end')
            self.display.winner_display.top_winner.configure(state='disabled')

            self.display.winner_display.random_winners.configure(state='normal')
            self.display.winner_display.random_winners.delete("0.0", 'end')
            self.display.winner_display.random_winners.configure(state='disabled')

            self.student_list.ninth_grade.var.set([])
            self.student_list.tenth_grade.var.set([])
            self.student_list.eleventh_grade.var.set([])
            self.student_list.twelfth_grade.var.set([])

    # all bindings and commands
    def bindings(self):
        # toggle buttons
        toggle = self.view.report_toggle
        toggle.end_quarter.configure(command=self.end_quarter)
        toggle.left_toggle.configure(command=self.left_arrow)
        toggle.right_toggle.configure(command=self.right_arrow)

        # display buttons
        self.display.create_pdf_button.configure(command=self.create_pdf_report)
        self.display.delete_report.configure(command=self.delete_report)

        # prize buttons
        self.prize_frame.add_button.configure(command=self.add_prize)
        self.prize_frame.delete_button.configure(command=self.delete_prize)
        self.prize_frame.edit_button.configure(command=self.edit_prize)

        # Fill field on double click
        self.table.tree.bind('<Double-1>', lambda e: self.fill_edit_field())

    def show_error(self, errors):
        error_string = ''
        for error in errors:
            error_string += '\n' + error
        tk.messagebox.showerror("Error", "The following data entry errors occurred:" + error_string)


class ReportFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.info_frame = ct.CTkFrame(self, fg_color="transparent")
        self.info_frame.grid(row=0, column=0, sticky='NEWS')
        self.name = ct.CTkLabel(self.info_frame, text='\nTitle', font=('arial', 20))
        self.name.grid(row=0, column=0, sticky='NEWS')

        self.date = ct.CTkLabel(self.info_frame, text='\nDate', font=('arial', 20))
        self.date.grid(row=0, column=1, sticky='NEWS')

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

        # Winner Box
        self.display.winner_display.rowconfigure(1, weight=0)

        # prizes: label, entries and buttons
        self.prize_frame.rowconfigure(0, weight=0)
        self.prize_frame.rowconfigure(3, weight=0)
        self.prize_frame.rowconfigure(4, weight=0)
        self.prize_frame.rowconfigure(5, weight=0)
        self.prize_frame.rowconfigure(6, weight=0)

        # Student list displays
        self.display.student_list.rowconfigure(0, weight=0)

        # Student list, Buttons
        self.display.rowconfigure(1, weight=0)
        self.display.rowconfigure(2, weight=0)

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
        self.label.grid(row=0, column=0, sticky='NEWS', padx=20, pady=20, columnspan=2)
        # Table
        self.prize_table = PrizeTable(self)
        self.prize_table.grid(row=1, column=0, sticky='NEWS', padx=30, columnspan=2)

        # Buttons
        font = ('arial', 15)
        corner_radius = 10
        pad_x = 30
        pad_y = 5
        height = 40
        self.add_button = ct.CTkButton(self, text='Add prize', font=font, corner_radius=corner_radius, height=height)
        self.add_button.grid(row=3, column=0, sticky='NEWS', padx=pad_x, pady=pad_y, columnspan=2)

        self.delete_button = ct.CTkButton(self, text='Delete prize', font=font, corner_radius=corner_radius,
                                          height=height, fg_color='#b30000', hover_color='#750000')
        self.delete_button.grid(row=4, column=0, sticky='NEWS', padx=pad_x, pady=pad_y, columnspan=2)

        self.edit_button = ct.CTkButton(self, text='Edit prize', font=font, corner_radius=corner_radius, height=height)
        self.edit_button.grid(row=5, column=0, sticky='NEWS', padx=pad_x, pady=(pad_y, pad_y), columnspan=2)

        self.name_entry = ct.CTkEntry(self, height=height // 20, placeholder_text=' Prize Name')
        self.name_entry.grid(row=6, column=0, sticky='NEWS', padx=(pad_x, 0), pady=(pad_y, pad_y))
        self.points_entry = ct.CTkEntry(self, height=height // 20, placeholder_text=' Points')
        self.points_entry.grid(row=6, column=1, sticky='NEWS', padx=(0, pad_x), pady=(pad_y, pad_y))
        # place_holder_bind_widget(self.name_entry)
        # place_holder_bind_widget(self.points_entry)


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
        columns = ("Prize Name", 'Points')
        self.tree["columns"] = columns
        for column in columns:
            self.tree.heading(column, text=column)
            if column == 'Points':
                self.tree.column(column, width=200, anchor='w')
            else:
                self.tree.column(column, width=200, anchor='w', minwidth=230)

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
        self.student_list.grid(row=0, column=0, sticky='NEWS', padx=20, pady=10, columnspan=2)

        self.winner_display = WinnersDisplay(self)
        self.winner_display.grid(row=1, column=0, sticky='NEWS', padx=20, pady=10, rowspan=2)

        self.create_pdf_button = ct.CTkButton(self, text='Create PDF', font=('arial', 15))
        self.create_pdf_button.grid(row=1, column=1, sticky='NEWS', padx=10, pady=10)

        self.delete_report = ct.CTkButton(self, text='Delete Report', font=('arial', 15),
                                          fg_color='#b30000', hover_color='#750000')
        self.delete_report.grid(row=2, column=1, sticky='NEWS', padx=10, pady=10)


class StudentList(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = 20
        sticky = 'NEWS'
        pad_x = 0
        pad_y = 0
        height = 10
        self.label_9 = ct.CTkLabel(self, text='Grade 9', font=('arial', font))
        self.label_9.grid(row=0, column=0, sticky=sticky, padx=pad_x, pady=pad_y)

        self.label_10 = ct.CTkLabel(self, text='Grade 10', font=('arial', font))
        self.label_10.grid(row=0, column=1, sticky=sticky, padx=pad_x, pady=pad_y)

        self.label_11 = ct.CTkLabel(self, text='Grade 11', font=('arial', font))
        self.label_11.grid(row=0, column=2, sticky=sticky, padx=pad_x, pady=pad_y)

        self.label_12 = ct.CTkLabel(self, text='Grade 12', font=('arial', font))
        self.label_12.grid(row=0, column=3, sticky=sticky, padx=pad_x, pady=pad_y)

        self.ninth_grade = self.student_list = tk.Listbox(self, height=height, borderwidth=10,
                                                          width=15, background="#343638", activestyle='dotbox',
                                                          font=("Helvetica", 15, "bold"), foreground="gray"
                                                          )
        self.ninth_grade.grid(row=1, column=0, sticky='NEWS')

        self.eleventh_grade = self.student_list = tk.Listbox(self, height=height, borderwidth=10,
                                                             width=15, background="#343638", activestyle='dotbox',
                                                             font=("Helvetica", 15, "bold"), foreground="gray"
                                                             )
        self.eleventh_grade.grid(row=1, column=1, sticky='NEWS')

        self.tenth_grade = self.student_list = tk.Listbox(self, height=height, borderwidth=10,
                                                          width=15, background="#343638", activestyle='dotbox',
                                                          font=("Helvetica", 15, "bold"), foreground="gray"
                                                          )
        self.tenth_grade.grid(row=1, column=2, sticky='NEWS')

        self.twelfth_grade = self.student_list = tk.Listbox(self, height=height, borderwidth=10,
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
        self.tenth_grade.configure(listvariable=self.tenth_grade.var)
        self.eleventh_grade.var = tk.StringVar(value=[])
        self.eleventh_grade.configure(listvariable=self.eleventh_grade.var)
        self.twelfth_grade.var = tk.StringVar(value=[])
        self.twelfth_grade.configure(listvariable=self.twelfth_grade.var)


class WinnersDisplay(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = 20
        sticky = 'NEWS'
        pad_x = 0
        pad_y = 0
        height = 72

        ct.CTkLabel(self, text='Overall winner', font=('arial', font)).grid(row=0, column=0, sticky=sticky, padx=pad_x,
                                                                            pady=pad_y)
        self.top_winner = ct.CTkTextbox(self, font=('Consolas', 12), state="disabled", height=height)
        self.top_winner.grid(row=1, column=0, sticky='NEWS', padx=10, pady=10)

        ct.CTkLabel(self, text='Random winners', font=('arial', font)).grid(row=0, column=1, sticky=sticky, padx=pad_x,
                                                                            pady=pad_y)
        self.random_winners = ct.CTkTextbox(self, font=('Consolas', 12), state="disabled", height=height)
        self.random_winners.grid(row=1, column=1, sticky='NEWS', padx=10, pady=10)


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
    ReportController(w)
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
