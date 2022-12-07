import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("500x500")


ttk.Button(root, text='btn').grid(row=0,column=0,  padx=50,pady=50)
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)










root.mainloop()