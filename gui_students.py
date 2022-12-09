import tkinter
from tkinter import ttk
import customtkinter as ct

# Combining both frames
class StudentsFrame(ct.CTkFrame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        # setting layout
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)

        StudentView(root).grid(row=0, column=0, sticky='NSEW')
        ToolWindow(root).grid(row=0, column=1, sticky='NSEW')

        #test
        #ct.CTkButton(root).grid(row=0, column=1, sticky='NSEW')



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
        for child in self.add_delete.winfo_children():
            self.add_delete.rowconfigure(child.grid_info()['row'], weight=1)
            self.add_delete.columnconfigure(child.grid_info()['column'], weight=1)

        for child in self.edit_frame.winfo_children():
            self.edit_frame.rowconfigure(child.grid_info()['row'], weight=1)
            self.edit_frame.columnconfigure(child.grid_info()['column'], weight=1)


class StudentView(ct.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        # Initializing and setting size
        tree = ttk.Treeview(root)
        tree.grid(row=0, column=0, sticky='NSEW')
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)

        # Adding stuff as a test. delete later
        for i in range(4):
            tree.insert("", "end", text=f"Item {i}")


if __name__ == "__main__":
    window = ct.CTk()
    # Setting size of the window
    window.geometry("500x500")
    ct.set_appearance_mode("light")  # Modes: system (default), light, dark
    ct.set_default_color_theme("dark-blue")

    StudentsFrame(window).grid(row=0, column=0, sticky='NSEW')
    #ToolWindow(window).grid(row=0, column=0, sticky='NSEW')
    #StudentView(window).grid(row=0, column=0, sticky='NSEW')
    window.mainloop()
