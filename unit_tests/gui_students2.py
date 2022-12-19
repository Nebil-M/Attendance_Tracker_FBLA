# This file has the GUI for the students but without classes, without object oriented programming.
import tkinter
from tkinter import ttk
import customtkinter as ct

root = ct.CTk()
root.geometry("1080x600")
root.title("Attendance Tracker")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)

students = ttk.Treeview(root)
students.insert("", "end", "student1", text="Bob")
students.grid(row=0, column=0, rowspan=3)


# Initializes the tabs
# The argument width and height refers to the size of the whole tab frame, not the tab labels
tabview = ct.CTkTabview(root, width=300, height=600)
tabview.grid(row=0, column=1, sticky="E")


# Creates the tab frames
tab_add_students = tabview.add("Add")
tab_edit_students = tabview.add("Edit")
# Sets the current visible tab to the "Add" tab
tabview.set("Add")

# The below widgets are in the tab_add_students frame
label_add_student = ct.CTkLabel(tab_add_students, text="Add a new student:")
label_add_student.grid(row=0, column=0, sticky="W")

student_id = ct.CTkEntry(tab_add_students, placeholder_text="Student ID")
student_id.grid(row=1, column=0, sticky="W")

first_name = ct.CTkEntry(tab_add_students, placeholder_text="First name")
first_name.grid(row=2, column=0, sticky="W")

last_name = ct.CTkEntry(tab_add_students, placeholder_text="Last name")
last_name.grid(row=3, column=0, sticky="W")

grade_level = ct.CTkEntry(tab_add_students, placeholder_text="Grade level")
grade_level.grid(row=4, column=0, sticky="W")

save = ct.CTkButton(tab_add_students, text="Save", width=120)
save.grid(row=5, column=0, sticky="SE")




# The below widgets are in the tab_edit_students frame
label_select_student = ct.CTkLabel(tab_edit_students, text="Select a student on the left:")
label_select_student.grid(row=0, column=0, sticky="W")

# need a label or something to display the student selected

label_edit_student = ct.CTkLabel(tab_edit_students, text="Edit student details:")
label_edit_student.grid(row=1, column=0, sticky="W")

student_id = ct.CTkEntry(tab_edit_students, placeholder_text="Student ID")
student_id.grid(row=2, column=0, sticky="W")

first_name = ct.CTkEntry(tab_edit_students, placeholder_text="First name")
first_name.grid(row=3, column=0, sticky="W")

last_name = ct.CTkEntry(tab_edit_students, placeholder_text="Last name")
last_name.grid(row=4, column=0, sticky="W")

grade_level = ct.CTkEntry(tab_edit_students, placeholder_text="Grade level")
grade_level.grid(row=5, column=0, sticky="W")

save = ct.CTkButton(tab_edit_students, text="Save", width=120)
save.grid(row=6, column=0, sticky="SE")


root.mainloop()
