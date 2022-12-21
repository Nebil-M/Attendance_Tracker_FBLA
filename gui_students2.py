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
        self.students = ttk.Treeview(root, columns=columns,
                                     displaycolumns=("Student ID", "Grade Level", "First name", "Last name", "Letter grade"),
                                     show="headings")  # btw show="headings" essentially hides the first "#0" column

        for column in columns:
            self.students.heading(column, text=column)
            self.students.column(column, width=200, anchor='w', minwidth=200)
        self.students.insert("", "end", text="student1", values=[1234, "Bob", "Ross", "A", 9], tags="student")
        self.students.insert("", "end", text="student2", values=[5678, "Sarah", "Smith", "A+", 9], tags="student")

        self.students.tag_configure("student", background='yellow')
        self.students.tag_bind("student", "<Double-1>", self.on_selection)
        self.students.grid(row=0, column=0)

    # Changes the label in the edit tab when a student is selected on the treeview
    def on_selection(self, event):
        selection = students_table.students.selection()
        # Checks if selection is empty or not
        if selection:
            # This variable stores the values of the selection
            # note: need to test if, with multiple students, what happens when multiple students are selected.
            text = students_table.students.item(selection[0])['values']
            # print(text, text[1], text[2], type(text))

            # The following lines fill out the Entry or Label widgets with the appropriate value from the Treeview's items
            # These use lowercase tabs because it's referring to the instance of the object (which is created at the bottom, after the class. this is bad practice(probably), i know).
            # if changed to Tabs, it throws an error about attributes (global? i thought self.attribute would be global but i guess not *shrugs*)
            # try to fix it if you want, just know i spent a good 60+ minutes getting this function figured out.
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

        # Initializes the tabs
        # The argument width and height refers to the size of the whole tab frame, not the tab labels
        self.tabview = ct.CTkTabview(root, width=300, height=600)
        self.tabview.grid(row=0, column=1, sticky="NES")

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
        ct.CTkLabel(self.tab_add_students, text="Add a new student:").grid(row=0, column=0, sticky="W")

        # Width for the Entrys are 160, while width for Save button is 80
        student_id = ct.CTkEntry(self.tab_add_students, placeholder_text="Student ID", width=160)
        student_id.grid(row=1, column=0, sticky="W")

        grade_level = ct.CTkEntry(self.tab_add_students, placeholder_text="Grade level", width=160)
        grade_level.grid(row=2, column=0, sticky="W")

        letter_grade = ct.CTkOptionMenu(self.tab_add_students, values=self.letter_grade_options, width=160)
        letter_grade.grid(row=3, column=0, sticky="W")
        letter_grade.set("Select a letter grade")

        first_name = ct.CTkEntry(self.tab_add_students, placeholder_text="First name", width=160)
        first_name.grid(row=4, column=0, sticky="W")

        last_name = ct.CTkEntry(self.tab_add_students, placeholder_text="Last name", width=160)
        last_name.grid(row=5, column=0, sticky="W")

        save = ct.CTkButton(self.tab_add_students, text="Save", width=80)
        save.grid(row=6, column=0, sticky="SE", pady=50)

    # Puts widgets on the Edit tab
    def edit_tab(self):
        # The below widgets are in the tab_edit_students frame
        ct.CTkLabel(self.tab_edit_students, text="Please select a student.").grid(row=0, column=0, sticky="W")

        # need to change the text in the label_student_selected to the student selected in the dropdown menu or the tree view.
        self.label_student_selected = ct.CTkLabel(self.tab_edit_students, text="Student selected: ")
        self.label_student_selected.grid(row=2, column=0, sticky="W", pady=10)

        ct.CTkLabel(self.tab_edit_students, text="Edit student details:").grid(row=3, column=0, sticky="W")

        ct.CTkLabel(self.tab_edit_students, text="Student ID").grid(row=4, column=0, sticky="W")

        self.student_id_value = ct.StringVar()
        self.student_id = ct.CTkEntry(self.tab_edit_students, textvariable=self.student_id_value,
                                      placeholder_text="Student ID", width=160)
        self.student_id.grid(row=5, column=0, sticky="W")

        ct.CTkLabel(self.tab_edit_students, text="Grade level").grid(row=6, column=0, sticky="W")

        self.grade_level_value = ct.StringVar()
        self.grade_level = ct.CTkEntry(self.tab_edit_students, textvariable=self.grade_level_value,
                                       placeholder_text="Grade level", width=160)
        self.grade_level.grid(row=7, column=0, sticky="W")


        ct.CTkLabel(self.tab_edit_students, text="Letter grade").grid(row=8, column=0, sticky="W")

        self.letter_grade_value = ct.StringVar()
        self.letter_grade = ct.CTkOptionMenu(self.tab_edit_students, variable=self.letter_grade_value,
                                             values=self.letter_grade_options, width=160)
        self.letter_grade.grid(row=9, column=0, sticky="W")
        self.letter_grade.set("Select a letter grade")

        ct.CTkLabel(self.tab_edit_students, text="First name").grid(row=10, column=0, sticky="W")

        self.first_name_value = ct.StringVar()
        self.first_name = ct.CTkEntry(self.tab_edit_students, textvariable=self.first_name_value,
                                      placeholder_text="First name", width=160)
        self.first_name.grid(row=11, column=0, sticky="W")

        ct.CTkLabel(self.tab_edit_students, text="Last name").grid(row=12, column=0, sticky="W")

        self.last_name_value = ct.StringVar(value=None)
        self.last_name = ct.CTkEntry(self.tab_edit_students, textvariable=self.last_name_value,
                                     placeholder_text="Last name", width=160)
        self.last_name.grid(row=13, column=0, sticky="W")

        save = ct.CTkButton(self.tab_edit_students, text="Save", width=80)
        save.grid(row=14, column=0, sticky="SE", pady=50)




if __name__ == "__main__":
    # Initializes the window
    root = ct.CTk()
    root.geometry("1080x600")
    root.title("Attendance Tracker")
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")

    tabs = Tabs(root)
    students_table = StudentsTable(root)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)

    root.mainloop()
