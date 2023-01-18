# This file has the GUI for the students but without classes, without object oriented programming.
import tkinter as tk
from tkinter import ttk
import customtkinter as ct
from student import student_manager
from Events import event_manager
from func_utils import *


class StudentController:
    def __init__(self, view):
        # view is StudentsFrame passed into Controller later on.
        self.view = view

        # Makes new local variables so it can access the table and tabs here
        self.students_table = self.view.table
        self.student_tabs = self.view.student_tabs

        # Populates the data into table
        self.update_students_table()

        # Binds the widgets
        self.widget_bindings()

    # Adds a new student by getting the info from the Entrys, creating a Student and updating the table
    def add_student(self):

        add_tab = self.student_tabs.add_tab

        validation = self.validate_data(add_tab)

        if validation == True:
            # Adds the student
            student_manager.add_student(int(add_tab.student_id.var.get()), add_tab.first_name.var.get(),
                                        add_tab.last_name.var.get(),
                                        add_tab.letter_grade.var.get(),
                                        int(add_tab.grade_level.get()))

            # Saves the student into the pkl file
            # commented out for testing
            student_manager.save_data()
            event_manager.save_data()

            # Updates the treeview with the new data
            self.update_students_table()

            self.clear_entries(self.student_tabs.add_tab)

        else:
            error_string = ''
            for error in validation:
                error_string += '\n' + error
            tk.messagebox.showerror("Error", "The following data entry errors occurred:" + error_string)

    def edit_student(self):
        # Gets the selected student's ID
        selection = self.students_table.tree.focus()

        edit_tab = self.student_tabs.edit_tab
        validation = self.validate_data(edit_tab, selection)

        if validation == True:
            # Assigns the current student details to the student variable
            student = student_manager.get_student(int(selection))

            # Assigns the new, updated student details to the student variable
            # Important! When assigning these new values, make sure you convert it to the right data type.
            student.student_id = int(edit_tab.student_id.var.get())
            student.first_name = edit_tab.first_name.var.get()
            student.last_name = edit_tab.last_name.var.get()
            student.letter_grade = edit_tab.letter_grade.var.get()
            student.grade_level = int(edit_tab.grade_level.var.get())

            # Saves the student into the pkl file
            # commented out for testing
            student_manager.save_data()
            event_manager.save_data()

            # Updates the treeview with the new data
            self.update_students_table()
            # Re-selects the student
            self.students_table.tree.focus(str(student.student_id))
        else:
            error_string = ''
            for error in validation:
                error_string += '\n' + error
            tk.messagebox.showerror("Error", "The following data entry errors occurred:" + error_string)

    def remove_student(self):
        # Gets the selected student's ID
        selection = self.students_table.tree.focus()

        edit_tab = self.student_tabs.edit_tab

        # Checks whether the selection is empty or not
        if selection:
            student = student_manager.get_student(int(selection))
            text = f"ID: {str(student.student_id)}\nGrade level: {str(student.grade_level)}\nFirst name: {student.first_name}\nLast name: {student.last_name}\nLetter grade: {student.letter_grade}\nPoints: {student.points}"
            confirmation = tk.messagebox.askokcancel("Delete student?",
                                                     message="Are you sure you want to delete this student?",
                                                     detail=text)

            if confirmation:
                # Removes the student
                student_manager.remove_student(int(selection))

                # Saves the data into the pkl file
                # commented out for testing
                student_manager.save_data()
                event_manager.save_data()
                # Updates the treeview with the new data
                self.update_students_table()
                # Cleans out the entries once the data is updated
                self.clear_entries(self.student_tabs.edit_tab)

    # Data validation!
    def validate_data(self, tab, selection=None):
        # Makes sure the tab is one of the tabs
        tabs = (self.student_tabs.add_tab, self.student_tabs.edit_tab)
        if tab not in tabs:
            raise Exception(f"Parameter tab should be one of the following values: {tabs}")

        data_entries = [tab.student_id.var.get(), tab.grade_level.var.get(), tab.first_name.var.get(),
                        tab.last_name.var.get(), tab.letter_grade.var.get()]
        errors = []
        student = None

        if selection:
            student = student_manager.get_student(int(selection))
        elif tab == self.student_tabs.edit_tab:
            errors.append('\tNo student is selected.')

        errors.append(student_manager.validate_id(data_entries[0], student))
        errors.append(student_manager.validate_grade_level(data_entries[1]))
        errors.append(student_manager.validate_first_name(data_entries[2]))
        errors.append(student_manager.validate_last_name(data_entries[3]))
        errors.append(student_manager.validate_letter_grade(data_entries[4]))

        # Gets rid of the True values in errors, which means the test passed.
        errors = [error for error in errors if not isinstance(error, bool)]

        return errors if errors else True

    # Clears or resets the entries
    def clear_entries(self, tab):
        # Makes sure the tab is one of the tabs
        tabs = (self.student_tabs.add_tab, self.student_tabs.edit_tab)
        if tab not in tabs:
            raise Exception(f"Parameter tab should be one of the following values: {tabs}")

        # Resets the label unique to the edit_tab
        if tab == self.student_tabs.edit_tab:
            tab.label_student_selected.configure(text=f"Student selected:  None")

        # Resets the entries
        tab.student_id.var.set("")
        tab.first_name.var.set("")
        tab.last_name.var.set("")
        tab.letter_grade.var.set("Select a letter grade")
        tab.grade_level.var.set("Select a grade level")

    # updates the treeview each time it is called. Call it anytime the model is changed.
    # It deletes all items from treeview and repopulates them
    def update_students_table(self):
        self.students_table.tree.delete(*self.students_table.tree.get_children())
        self.students_table.load_students(student_manager.students)

    # Changes the label in the edit tab when a student is selected on the treeview
    def on_selection(self, event=None):
        # Gets the selected item
        selection = self.students_table.tree.focus()
        edit_tab = self.student_tabs.edit_tab
        # Checks if selection is empty or not
        if selection:
            # This variable stores the values of the selection
            student = student_manager.get_student(int(selection))

            # Changes the current tab to the Edit tab
            self.student_tabs.tabview.set("Edit")

            # The following lines fill out the Entry or Label widgets with the appropriate value from the Treeview's items
            edit_tab.label_student_selected.configure(
                text=f"Student selected:  {student.first_name} {student.last_name}")
            edit_tab.student_id.var.set(student.student_id)
            edit_tab.grade_level.var.set(student.grade_level)
            edit_tab.letter_grade.var.set(student.letter_grade)
            edit_tab.first_name.var.set(student.first_name)
            edit_tab.last_name.var.set(student.last_name)

    def widget_bindings(self):
        self.students_table.tree.tag_bind("student", '<Double-1>', self.on_selection)
        self.student_tabs.add_tab.save.configure(command=self.add_student)
        self.student_tabs.edit_tab.save.configure(command=self.edit_student)
        self.student_tabs.edit_tab.delete.configure(command=self.remove_student)


# This class creates and grids all the widgets from other classes. The main purpose is to use the variables here.
class StudentsFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Makes it resizeable
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=1)

        self.table = StudentsTable(self)
        self.table.grid(row=0, column=0, sticky='NEWS', padx=10, pady=30)

        # The tabs
        self.student_tabs = Tabs(self)
        self.student_tabs.grid(row=0, column=1, sticky='NEWS')

        # Fixing the bug with placeholders for all entries that is a child of this widget.
        place_holder_bind_all(self)


class StudentsTable(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Treeview styling
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', fieldbackground='#343638', rowheight=40)
        style.configure('Treeview.Heading', background="#343638", foreground='gray', font=('Helvetica', 20, 'bold'),
                        fieldbackground='#343638')

        # columns is in the proper order for the student object to just dump its data into the tree view.
        # displaycolumns is the order the columns are shown.
        columns = ("Student ID", "First name", "Last name", "Letter grade", "Grade Level", "Points")

        # Initializes and grids the treeview
        self.tree = ttk.Treeview(self, selectmode="browse", columns=columns, displaycolumns=(
            "Student ID", "Grade Level", "First name", "Last name", "Letter grade", "Points"),
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
            if column == "Grade Level":
                self.tree.column(column, width=70, anchor='center', minwidth=80)
            else:
                self.tree.column(column, width=180, anchor='center', minwidth=200)

    # Do NOT use this function to add students. This only affects the treeview, not the actual data. Only use for testing.
    def add_student(self, student):
        values = (student.student_id, student.first_name, student.last_name, student.letter_grade, student.grade_level)
        student_id = str(student.student_id)
        self.tree.insert("", 'end', student_id, text=student_id, values=values, tags=("ttk", "student"))

    def load_students(self, students):
        # This part allows the students to be sorted
        list_of_students = []
        for student in students:
            values = (
                student.student_id, student.first_name, student.last_name, student.letter_grade, student.grade_level,
                student.points)
            list_of_students.append(values)
        # Sorts the list by grade level, then by number of points
        list_of_students.sort(reverse=True, key=lambda x: (x[4], x[5]))

        # Adds the students into the treeview
        for student in list_of_students:
            student_id = str(student[0])
            self.tree.insert("", 'end', student_id, text=student_id, values=student, tags=("ttk", "student"))
        self.tree.tag_configure("ttk", font=('Helvetica', 20, 'bold'), foreground='gray74', background='#343638')


class Tabs(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Initializes the tabs
        self.tabview = ct.CTkTabview(self)
        self.tabview.grid(row=0, column=0, sticky="NEWS")

        # Creates the tab frames
        self.tabview.add("Add")
        self.tabview.add("Edit")
        # Sets the current visible tab to the "Add" tab
        self.tabview.set("Add")

        # Adds the widgets contained in the AddTab object and EditTab to the frame
        # There are two arguments because it throws an error otherwise.
        self.add_tab = AddTab(self.tabview.tab("Add"), self.tabview.tab("Add"))
        self.edit_tab = EditTab(self.tabview.tab("Edit"), self.tabview.tab("Edit"))


# Creates the layout of the content in the add tab
class AddTab(ct.CTkFrame):
    def __init__(self, tab, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(fg_color="transparent")

        self.letter_grade_options = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
        self.grade_level_options = ['9', '10', '11', '12']

        # Creates the widgets
        self.student_id = ct.CTkEntry(tab, placeholder_text="Student ID", width=160)
        self.grade_level = ct.CTkOptionMenu(tab, values=self.grade_level_options, width=160)
        self.first_name = ct.CTkEntry(tab, placeholder_text="First name", width=160)
        self.last_name = ct.CTkEntry(tab, placeholder_text="Last name", width=160)
        self.letter_grade = ct.CTkOptionMenu(tab, values=self.letter_grade_options, width=160)
        self.save = ct.CTkButton(tab, text="Save", width=80)

        # Grids the widgets and adds the labels
        pad = (0, 10)
        ct.CTkLabel(tab, text="Add a new student:").grid(row=0, column=0, sticky="W", pady=(10, 20))
        ct.CTkLabel(tab, text="Student ID").grid(row=1, column=0, sticky="W")
        self.student_id.grid(row=2, column=0, sticky="W", pady=pad)
        ct.CTkLabel(tab, text="Grade level").grid(row=3, column=0, sticky="W")
        self.grade_level.grid(row=4, column=0, sticky="W", pady=pad)
        ct.CTkLabel(tab, text="First name").grid(row=5, column=0, sticky="W")
        self.first_name.grid(row=6, column=0, sticky="W", pady=pad)
        ct.CTkLabel(tab, text="Last name").grid(row=7, column=0, sticky="W")
        self.last_name.grid(row=8, column=0, sticky="W", pady=pad)
        ct.CTkLabel(tab, text="Letter grade").grid(row=9, column=0, sticky="W")
        self.letter_grade.grid(row=10, column=0, sticky="W", pady=pad)
        # the save button's y padding is very high, to make it appear in the same place in both the add and edit tab.
        self.save.grid(row=11, column=0, sticky="SW", pady=(105, 10), padx=(200, 0))

        # applying a weight of 1 to all cells
        limited_weight_cells(self)
        # add vars to all entries
        self.add_vars_to_entries()

    # Gives the entries variables so we can access their data later
    def add_vars_to_entries(self):
        self.student_id.var = tk.StringVar()
        self.student_id.configure(textvariable=self.student_id.var)
        self.grade_level.var = tk.StringVar(value="Select a grade level")
        self.grade_level.configure(variable=self.grade_level.var)
        self.first_name.var = tk.StringVar()
        self.first_name.configure(textvariable=self.first_name.var)
        self.last_name.var = tk.StringVar()
        self.last_name.configure(textvariable=self.last_name.var)
        self.letter_grade.var = tk.StringVar(value="Select a letter grade")
        self.letter_grade.configure(variable=self.letter_grade.var)

        # The following lines are just for testing purposes.
        # self.student_id.var.set("58010001")
        # self.grade_level.var.set("9")
        # self.first_name.var.set("Foo")
        # self.last_name.var.set("Bar")
        # self.letter_grade.var.set("B")


# Creates the layout of the content in the edit tab
class EditTab(ct.CTkFrame):
    def __init__(self, tab, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(fg_color="transparent")

        self.grade_level_options = ['9', '10', '11', '12']
        self.letter_grade_options = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]

        # Creates the widgets
        self.label_student_selected = ct.CTkLabel(tab, text="Student selected: None")
        self.student_id = ct.CTkEntry(tab, placeholder_text="Student ID", width=160)
        self.grade_level = ct.CTkOptionMenu(tab, values=self.grade_level_options, width=160)
        self.first_name = ct.CTkEntry(tab, placeholder_text="First name", width=160)
        self.last_name = ct.CTkEntry(tab, placeholder_text="Last name", width=160)
        self.letter_grade = ct.CTkOptionMenu(tab, values=self.letter_grade_options, width=160)
        self.delete = ct.CTkButton(tab, text="Delete", width=80, fg_color='#b30000', hover_color='#750000')
        self.save = ct.CTkButton(tab, text="Save", width=80)

        # Grids the widgets and makes the labels
        pad = (0, 10)
        ct.CTkLabel(tab, text="Edit student details:").grid(row=0, column=0, sticky="W", pady=10)
        ct.CTkLabel(tab, text="Please double click on the left to select a student.").grid(row=1, column=0, sticky="W",
                                                                                           columnspan=2)
        self.label_student_selected.grid(row=2, column=0, sticky="W", pady=(10, 0))
        ct.CTkLabel(tab, text="Student ID").grid(row=4, column=0, sticky="W", pady=(10, 0))
        self.student_id.grid(row=5, column=0, sticky="W", pady=pad)
        ct.CTkLabel(tab, text="Grade level").grid(row=6, column=0, sticky="W")
        self.grade_level.grid(row=7, column=0, sticky="W", pady=pad)
        ct.CTkLabel(tab, text="First name").grid(row=8, column=0, sticky="W")
        self.first_name.grid(row=9, column=0, sticky="W", pady=pad)
        ct.CTkLabel(tab, text="Last name").grid(row=10, column=0, sticky="W")
        self.last_name.grid(row=11, column=0, sticky="W", pady=pad)
        ct.CTkLabel(tab, text="Letter grade").grid(row=12, column=0, sticky="W")
        self.letter_grade.grid(row=13, column=0, sticky="W", pady=pad)
        self.delete.grid(row=14, column=0, sticky="W", pady=(40, 10))
        self.save.grid(row=14, column=1, sticky="SW", pady=(40, 10), padx=(40, 0))

        # add vars to all entries
        self.add_vars_to_entries()

    # Gives the entries variables so we can access their data later
    def add_vars_to_entries(self):
        self.student_id.var = tk.StringVar()
        self.student_id.configure(textvariable=self.student_id.var)
        self.grade_level.var = tk.StringVar(value="Select a grade level")
        self.grade_level.configure(variable=self.grade_level.var)
        self.first_name.var = tk.StringVar()
        self.first_name.configure(textvariable=self.first_name.var)
        self.last_name.var = tk.StringVar()
        self.last_name.configure(textvariable=self.last_name.var)
        self.letter_grade.var = tk.StringVar(value="Select a letter grade")
        self.letter_grade.configure(variable=self.letter_grade.var)


if __name__ == "__main__":
    # Initializes the window
    window = ct.CTk()
    window.geometry()
    window.title("Attendance Tracker")
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")

    s = StudentsFrame(window)
    s.grid(row=0, column=0, sticky='NEWS')

    controller = StudentController(s)

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)

    # Sets the minimum size of the window
    # window.minsize(875, 575)

    window.mainloop()
