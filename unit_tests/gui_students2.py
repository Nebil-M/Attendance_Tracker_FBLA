# This file has the GUI for the students but without classes, without object oriented programming.
from tkinter import ttk
import customtkinter as ct


class StudentsTable(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Treeview styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', fieldbackground='#343638', rowheight=40)
        style.configure('Treeview.Heading', background="#343638", foreground='gray', font=('Helvetica', 20, 'bold'),
                        fieldbackground='#343638')

        # Initializes the treeview
        columns = ("Student ID", "First name", "Last name", "Letter grade", "Grade Level")
        # columns and display columns are different. columns is in the proper order for the student object to just dump its data
        # into the tree view.
        # however, i wanted the treeview to re-arrange the columns in a more logical fashion,
        # so the order for display columns is different from columns.
        students = ttk.Treeview(root, columns=columns,
                                displaycolumns=("Student ID", "Grade Level", "First name", "Last name", "Letter grade"),
                                show="headings")  # btw show="headings" essentially hides the first "#0" column

        for column in columns:
            students.heading(column, text=column)
            students.column(column, width=200, anchor='w', minwidth=200)
        students.insert("", "end", text="student1", values=[1234, "Bob", "Ross", "A", 9])

        students.grid(row=0, column=0)


class Tabs(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.letter_grade_values = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]

        # Initializes the tabs
        # The argument width and height refers to the size of the whole tab frame, not the tab labels
        self.tabview = ct.CTkTabview(root, width=300, height=600)
        self.tabview.grid(row=0, column=1, sticky="NEWS")

        # Creates the tab frames
        self.tab_add_students = self.tabview.add("Add")
        self.tab_edit_students = self.tabview.add("Edit")
        # Sets the current visible tab to the "Add" tab
        self.tabview.set("Add")

        # These functions put the widgets onto the tab frames
        self.add_tab()
        self.edit_tab()

    # Puts widgets on the Add tab
    def add_tab(self):
        # The below widgets are in the tab_add_students frame
        label_add_student = ct.CTkLabel(self.tab_add_students, text="Add a new student:")
        label_add_student.grid(row=0, column=0, sticky="W")

        student_id = ct.CTkEntry(self.tab_add_students, placeholder_text="Student ID")
        student_id.grid(row=1, column=0, sticky="W")

        grade_level = ct.CTkEntry(self.tab_add_students, placeholder_text="Grade level")
        grade_level.grid(row=2, column=0, sticky="W")

        letter_grade = ct.CTkComboBox(self.tab_add_students, values=self.letter_grade_values)
        letter_grade.grid(row=3, column=0, sticky="W")
        letter_grade.set("Select a letter grade")

        first_name = ct.CTkEntry(self.tab_add_students, placeholder_text="First name")
        first_name.grid(row=4, column=0, sticky="W")

        last_name = ct.CTkEntry(self.tab_add_students, placeholder_text="Last name")
        last_name.grid(row=5, column=0, sticky="W")

        save = ct.CTkButton(self.tab_add_students, text="Save", width=120)
        save.grid(row=6, column=0, sticky="SE")

    # Puts widgets on the Edit tab
    def edit_tab(self):
        # The below widgets are in the tab_edit_students frame
        label_select_student = ct.CTkLabel(self.tab_edit_students,
                                           text="Select a student on the left or use the drop down menu below:")
        label_select_student.grid(row=0, column=0, sticky="W")

        # need to set the values of student_selected to the names of the students
        student_selected = ct.CTkComboBox(self.tab_edit_students)
        student_selected.grid(row=1, column=0, sticky="W")

        # need to change the text in the label_student_selected to the student selected in the dropdown menu or the tree view.
        label_student_selected = ct.CTkLabel(self.tab_edit_students, text="Student selected: ")
        label_student_selected.grid(row=2, column=0, sticky="W")

        label_edit_student = ct.CTkLabel(self.tab_edit_students, text="Edit student details:")
        label_edit_student.grid(row=3, column=0, sticky="W")

        student_id = ct.CTkEntry(self.tab_edit_students, placeholder_text="Student ID")
        student_id.grid(row=4, column=0, sticky="W")

        grade_level = ct.CTkEntry(self.tab_edit_students, placeholder_text="Grade level")
        grade_level.grid(row=5, column=0, sticky="W")

        letter_grade = ct.CTkComboBox(self.tab_edit_students, values=self.letter_grade_values)
        letter_grade.grid(row=6, column=0, sticky="W")
        letter_grade.set("Select a letter grade")

        first_name = ct.CTkEntry(self.tab_edit_students, placeholder_text="First name")
        first_name.grid(row=7, column=0, sticky="W")

        last_name = ct.CTkEntry(self.tab_edit_students, placeholder_text="Last name")
        last_name.grid(row=8, column=0, sticky="W")

        save = ct.CTkButton(self.tab_edit_students, text="Save", width=120)
        save.grid(row=9, column=0, sticky="SE")


if __name__ == "__main__":
    # Initializes the window
    root = ct.CTk()
    root.geometry("1080x600")
    root.title("Attendance Tracker")
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")

    StudentsTable(root)
    Tabs(root)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)

    root.mainloop()
