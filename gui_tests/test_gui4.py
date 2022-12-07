from tkinter import *
from tkinter import ttk
import customtkinter as ct


class Login(ct.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        main_frame = ct.CTkFrame(self)
        main_frame.grid(row=0, column=0, sticky="NSEW")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        ct.CTkLabel(main_frame, text='Login Screen', font=("arial", 30)).grid(row=0, column=0, sticky="NSEW", pady=12, padx=10)
        username = ct.CTkEntry(main_frame, placeholder_text='Username', font=("arial", 25))
        username.grid(row=1, column=0, sticky="NSEW", pady=12, padx=30)
        password = ct.CTkEntry(main_frame, placeholder_text='Password', font=("arial", 25))
        password.grid(row=2, column=0, sticky="NSEW", pady=12, padx=30)
        remember_me_box = ct.CTkCheckBox(main_frame, text='Remember me')
        remember_me_box.grid(row=3, column=0, sticky="NSEW", pady=12, padx=40)
        btn_login = ct.CTkButton(main_frame, text='Login', compound="top")
        btn_login.grid(row=4, column=0, sticky="NSEW", pady=12, padx=30)


        for child in main_frame.winfo_children():
            main_frame.rowconfigure(child.grid_info()['row'], weight=1, minsize=130)
            main_frame.columnconfigure(child.grid_info()['column'], weight=1, minsize=600)



if __name__ == "__main__":
    root = ct.CTk()
    root.geometry("700x740")
    root.title("Login")
    ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ct.set_default_color_theme("dark-blue")
    Login(root).pack(padx=0, pady=0,expand=True, anchor='center')

    root.mainloop()