import tkinter
from tkinter import ttk
import customtkinter as ct
from func_utils import weight_cells_1



# Combining both frames
class StudentsFrame(ct.CTkFrame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)

        StudentView(self).grid(row=0, column=0, sticky='NSEW')
        ToolWindow(self).grid(row=0, column=1, sticky='NSEW')

class ToolWindow(ct.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        # create two frames for add-delete and editing students
        self.add_delete = ct.CTkFrame(self)
        self.edit_frame = ct.CTkFrame(self)
        # manage their geometry
        self.add_delete.grid(column=0, row=0, sticky='NSEW')
        self.edit_frame.grid(column=0, row=1, sticky='NSEW')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # Buttons
        ct.CTkButton(self.add_delete, text='ADD').grid(column=0, row=0, sticky='NSEW', padx=20, pady=20)
        ct.CTkButton(self.edit_frame, text='Edit').grid(column=0, row=0, sticky='NSEW', padx=20, pady=20)

        # Adding weight to all cells in both frames
        weight_cells_1(self)


class StudentView(ct.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        # Initializing and setting size
        tree = ttk.Treeview(self)
        tree.grid(row=0, column=0, sticky='NSEW')

        # Adding stuff as a test. delete later
        for i in range(4):
            tree.insert("", "end", text=f"Item {i}")



if __name__ == "__main__":
    window = ct.CTk()
    # Setting size of the window
    #window.geometry("500x500")
    ct.set_appearance_mode("light")  # Modes: system (default), light, dark
    ct.set_default_color_theme("dark-blue")

    StudentsFrame(window).grid(row=0, column=0, sticky='NSEW')
    #ToolWindow(window).grid(row=0, column=0, sticky='NSEW')
    #StudentView(window).grid(row=0, column=0, sticky='NSEW')

    # Making the widgets resizable
    window.rowconfigure(0,weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
