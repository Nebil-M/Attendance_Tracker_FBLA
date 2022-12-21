import customtkinter as ct
from tkinter import ttk



if __name__ == '__main__':
    ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ct.set_default_color_theme("dark-blue")
    root = ct.CTk()
    root.geometry("500x500")

    root.mainloop()
