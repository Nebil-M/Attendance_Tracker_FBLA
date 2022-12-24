# This file has the GUI for the students but without classes, without object oriented programming.
from tkinter import ttk
import customtkinter as ct
from student import *


class StudentsFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.table = StudentsTable(self)
        self.table.grid(row=0, column=0, sticky='NEWS', padx=10, pady=30)

        sm = StudentManager()
        self.table.load_students(sm.students)

        myStudent = Student(58010001, "abcdefghijklmnopqrstuvwxyz", "test", "A", 11)
        self.table.add_student(myStudent)


class StudentsTable(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, minsize=200)

        # Treeview styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', fieldbackground='#343638', rowheight=40)
        style.configure('Treeview.Heading', background="#343638", foreground='gray', font=('Helvetica', 20, 'bold'),
                        fieldbackground='#343638')

        # columns is in the proper order for the student object to just dump its data into the tree view.
        # displaycolumns is the order the columns are shown.
        columns = ("Student ID", "First name", "Last name", "Letter grade", "Grade Level")

        # Initializes and grids the treeview
        self.tree = ttk.Treeview(self, selectmode="browse", columns=columns, displaycolumns=(
            "Student ID", "Grade Level", "First name", "Last name", "Letter grade"),
                                 show="headings")  # btw show="headings" essentially hides the first "#0" column
        self.tree.grid(row=0, column=0, sticky='NEWS')

        # Initializes and grids the scrollbars
        self.scroll_x = ct.CTkScrollbar(self, orientation="horizontal", command=self.tree.xview)
        self.scroll_y = ct.CTkScrollbar(self, orientation="vertical", command=self.tree.yview)
        self.tree.configure(xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.grid(row=1, column=0, sticky="EW")
        self.scroll_y.grid(row=0, column=1, sticky="NS")

        # Styling for the treeview
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=200, anchor='center', minwidth=200)

    def add_student(self, student):
        values = (student.student_id, student.first_name, student.last_name, student.letter_grade, student.grade_level)
        student_id = str(student.student_id)
        self.tree.insert("", 'end', student_id, text=student_id, values=values, tags=("ttk", "student"))

    def load_students(self, students):
        for student in students:
            values = (
                student.student_id, student.first_name, student.last_name, student.letter_grade, student.grade_level)
            student_id = str(student.student_id)
            self.tree.insert("", 'end', student_id, text=student_id, values=values, tags=("ttk", "student"))
        self.tree.tag_configure("ttk", font=('Helvetica', 20, 'bold'), foreground='gray74', background='#343638')
        # self.tree.tag_configure("student", background='yellow')
        self.tree.tag_bind("student", "<Double-1>", self.on_selection)

    # Changes the label in the edit tab when a student is selected on the treeview
    def on_selection(self, event):
        # Gets the selected item
        selection = self.tree.focus()
        # Checks if selection is empty or not
        if selection:
            # This variable stores the values of the selection
            text = self.tree.item(selection)['values']
            # print(text, text[1], text[2], type(text))

            # Changes the current tab to the Edit tab
            tabs.tabview.set("Edit")
            # The following lines fill out the Entry or Label widgets with the appropriate value from the Treeview's items
            # These use lowercase tabs because it's referring to the instance of the object (which is created at the bottom, after the class. this is bad practice(probably), i know).
            tabs.label_student_selected.configure(text=f"Student selected:  {text[1]} {text[2]}")
            tabs.student_id_value.set(text[0])
            tabs.grade_level_value.set(text[4])
            tabs.letter_grade_value.set(text[3])
            tabs.first_name_value.set(text[1])
            tabs.last_name_value.set(text[2])


class Tabs(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.letter_grade_options = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        # Initializes the tabs
        # The argument width and height refers to the size of the whole tab frame, not the tab labels
        self.tabview = ct.CTkTabview(root, width=200)
        self.tabview.grid(row=0, column=1, sticky="NES")

        # Creates the tab frames
        self.tab_add_students = self.tabview.add("Add")
        self.tab_edit_students = self.tabview.add("Edit")
        # Sets the current visible tab to the "Add" tab
        self.tabview.set("Add")

        pad = (0, 10)
        # The below widgets are in the tab_add_students frame
        ct.CTkLabel(self.tab_add_students, text="Add a new student:").grid(row=0, column=0, sticky="W", pady=(10, 20))

        # Width for the Entrys are 160, while width for Save button is 80
        # Student ID
        ct.CTkLabel(self.tab_add_students, text="Student ID").grid(row=1, column=0, sticky="W")
        student_id = ct.CTkEntry(self.tab_add_students, placeholder_text="Student ID", width=160)
        student_id.grid(row=2, column=0, sticky="W", pady=pad)

        # Grade level
        ct.CTkLabel(self.tab_add_students, text="Grade level").grid(row=3, column=0, sticky="W")
        grade_level = ct.CTkEntry(self.tab_add_students, placeholder_text="Grade level", width=160)
        grade_level.grid(row=4, column=0, sticky="W", pady=pad)

        # First name
        ct.CTkLabel(self.tab_add_students, text="First name").grid(row=5, column=0, sticky="W")
        first_name = ct.CTkEntry(self.tab_add_students, placeholder_text="First name", width=160)
        first_name.grid(row=6, column=0, sticky="W", pady=pad)

        # Last name
        ct.CTkLabel(self.tab_add_students, text="Last name").grid(row=7, column=0, sticky="W")
        last_name = ct.CTkEntry(self.tab_add_students, placeholder_text="Last name", width=160)
        last_name.grid(row=8, column=0, sticky="W", pady=pad)

        # Letter grade
        ct.CTkLabel(self.tab_add_students, text="Letter grade").grid(row=9, column=0, sticky="W")
        letter_grade = ct.CTkOptionMenu(self.tab_add_students, values=self.letter_grade_options, width=160)
        letter_grade.grid(row=10, column=0, sticky="W", pady=pad)
        letter_grade.set("Select a letter grade")

        # Save
        save = ct.CTkButton(self.tab_add_students, text="Save", width=80)
        save.grid(row=11, column=0, sticky="SE", pady=(50, 10))

        # The below widgets are in the tab_edit_students frame
        # Text labels that give the user instructions.
        ct.CTkLabel(self.tab_edit_students, text="Edit student details:").grid(row=0, column=0, sticky="W", pady=10)
        ct.CTkLabel(self.tab_edit_students, text="Please select a student.").grid(row=1, column=0, sticky="W")

        # Text label that dynamically changes as a student is selected in the treeview.
        self.label_student_selected = ct.CTkLabel(self.tab_edit_students, text="Student selected: ")
        self.label_student_selected.grid(row=2, column=0, sticky="W", pady=(10, 0))

        # Student ID
        ct.CTkLabel(self.tab_edit_students, text="Student ID").grid(row=4, column=0, sticky="W", pady=(10, 0))
        self.student_id_value = ct.StringVar()
        self.student_id = ct.CTkEntry(self.tab_edit_students, textvariable=self.student_id_value,
                                      placeholder_text="Student ID", width=160)
        self.student_id.grid(row=5, column=0, sticky="W", pady=pad)

        # Grade level
        ct.CTkLabel(self.tab_edit_students, text="Grade level").grid(row=6, column=0, sticky="W")
        self.grade_level_value = ct.StringVar()
        self.grade_level = ct.CTkEntry(self.tab_edit_students, textvariable=self.grade_level_value,
                                       placeholder_text="Grade level", width=160)
        self.grade_level.grid(row=7, column=0, sticky="W", pady=pad)

        # First name
        ct.CTkLabel(self.tab_edit_students, text="First name").grid(row=8, column=0, sticky="W")
        self.first_name_value = ct.StringVar()
        self.first_name = ct.CTkEntry(self.tab_edit_students, textvariable=self.first_name_value,
                                      placeholder_text="First name", width=160)
        self.first_name.grid(row=9, column=0, sticky="W", pady=pad)

        # Last name
        ct.CTkLabel(self.tab_edit_students, text="Last name").grid(row=10, column=0, sticky="W")
        self.last_name_value = ct.StringVar(value=None)
        self.last_name = ct.CTkEntry(self.tab_edit_students, textvariable=self.last_name_value,
                                     placeholder_text="Last name", width=160)
        self.last_name.grid(row=11, column=0, sticky="W", pady=pad)

        # Letter grade
        ct.CTkLabel(self.tab_edit_students, text="Letter grade").grid(row=12, column=0, sticky="W")
        self.letter_grade_value = ct.StringVar()
        self.letter_grade = ct.CTkOptionMenu(self.tab_edit_students, variable=self.letter_grade_value,
                                             values=self.letter_grade_options, width=160)
        self.letter_grade.grid(row=13, column=0, sticky="W", pady=pad)
        self.letter_grade.set("Select a letter grade")

        # Save
        save = ct.CTkButton(self.tab_edit_students, text="Save", width=80)
        save.grid(row=14, column=0, sticky="SE", pady=(50, 10))


if __name__ == "__main__":
    # Initializes the window
    root = ct.CTk()
    root.geometry()
    root.title("Attendance Tracker")
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")

    # don't change the variable name tabs or move it around or else the program will explode.
    tabs = Tabs(root)

    # students_table = StudentsTable(root)
    StudentsFrame(root).grid(row=0, column=0)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    root.minsize(875, 525)

    root.mainloop()
