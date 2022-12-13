from tkinter import *
from tkinter import ttk
import customtkinter as ct

class Calculator:

    def __init__(self, root):

        # Frames
        mainframe = ct.CTkFrame(root)
        mainframe.grid(row=0, column=0, sticky="NSEW", pady=20, padx=20)
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)
        self.box = ct.CTkEntry(mainframe, font=('arial', 30))
        buttons_frame = ct.CTkFrame(mainframe)

        # Set grid
        self.box.grid(row=0, column=0, sticky="NSEW")
        buttons_frame.grid(row=1, column=0, sticky="NSEW", pady=20)

        # RowConfig
        Grid.rowconfigure(mainframe, 0, weight=1)
        Grid.rowconfigure(mainframe, 1, weight=5)
        Grid.columnconfigure(mainframe, 0, weight=1)
        # Buttons
        # Numbers
        n = 1
        for row in range(1, 4):
            for column in range(3):
                ct.CTkButton(buttons_frame, command=lambda n=n: self.add_to_box(str(n)), text=str(n)).grid(column=column,
                                                                                                         row=row,
                                                                                                         sticky="NSEW")
                Grid.rowconfigure(buttons_frame, row, weight=1)
                Grid.columnconfigure(buttons_frame, column, weight=1)
                n += 1
        # symbols
        symbols = ["+", '-', "*", "/"]

        rows = len(symbols)
        for row in range(rows):
            symbol = symbols[row]
            ct.CTkButton(buttons_frame, command=lambda symbol=symbol: self.add_to_box(symbol), text=symbol).grid(column=4,
                                                                                                               row=row,
                                                                                                               sticky="NSEW")
            Grid.rowconfigure(buttons_frame, row, weight=1)
            Grid.columnconfigure(buttons_frame, 4, weight=1)

        # last row
        last_row_sy = ["**", "0", "."]
        for column in range(3):
            s = last_row_sy[column]
            ct.CTkButton(buttons_frame, command=lambda sy=s: self.add_to_box(sy), text=s).grid(column=column, row=5,
                                                                                             sticky="NSEW")
            Grid.rowconfigure(buttons_frame, 5, weight=1)
            Grid.columnconfigure(buttons_frame, column, weight=1)

        # equals func
        ct.CTkButton(buttons_frame, command=self.calculate, text='=').grid(column=4, row=5, sticky="NSEW")

        ##
        ct.CTkButton(buttons_frame, command=lambda: self.box.delete(0, END), text='Clear').grid(column=0, row=0,
                                                                                              sticky="NSEW")
        ct.CTkButton(buttons_frame, command=lambda: self.box.delete(self.box.index("end") - 1), text='del').grid(column=1,
                                                                                                               row=0,
                                                                                                               sticky="NSEW")
        ct.CTkButton(buttons_frame, command=lambda: self.box.insert(END, '%'), text='%').grid(column=2, row=0,
                                                                                            sticky="NSEW")

        for child in buttons_frame.winfo_children():
            child.grid(padx=2, pady=2)

    def calculate(self):
        ans = eval(self.box.get())
        self.box.delete(0, END)
        self.box.insert(0, ans)

    def add_to_box(self, symbol):
        self.box.insert(END, symbol)


if __name__ == '__main__':
    ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ct.set_default_color_theme("dark-blue")
    root = ct.CTk()
    root.geometry("500x500")
    Calculator(root)
    root.mainloop()
