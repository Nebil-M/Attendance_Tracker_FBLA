import tkinter as tk
from tkinter import ttk
import customtkinter as ct
from func_utils import weight_cells_1

if __name__ == '__main__':
    ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ct.set_default_color_theme("dark-blue")
    root = ct.CTk()
    root.geometry("500x500")
    ctk_button = ct.CTkButton(root)
    ctk_button.grid()

    print(ctk_button.cget("fg_color"))
    root.mainloop()
