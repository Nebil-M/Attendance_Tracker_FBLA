import tkinter as tk
from tkinter import ttk


class Login():
    def __init__(self, root):
        self.frame = ttk.Frame(root, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky= NSEW)
        self.l1 = ttk.Label(self.frame, text='Name: ')
        self.e1 = ttk.Entry(self.frame, text='')
        self.l2 = ttk.Label(self.frame, text='Password: ')
        self.e2 = ttk.Entry(self.frame, text='')
        self.l1.grid(column=0, row=0)
        self.l2.grid(column=0, row=1)
        self.e1.grid(column=1, row=0)
        self.e2.grid(column=1, row=1)


        print(type(self.e2.grid(column=1, row=1)))


if __name__ == '__main__':
    root = tk.Tk()
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    app = Login(root)
    root.mainloop()
