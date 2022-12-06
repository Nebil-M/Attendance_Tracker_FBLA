from tkinter import*

import random

root = Tk()
root.title("Data Table")
root.geometry("500x500")

name = ["John", "James", "Jack", "Jill", "Joe", "Jenny", "Jade", "Jasmine", "Jasmin", "Jade"]
age = []

for i in range(10):
    age.append(random.randint(1,100))

name_label = Label(root, text="Name")
name_label.grid(row=0, column=0)

age_label = Label(root, text="Age")
age_label.grid(row=0, column=1)

for i in range(10):
    name_label = Label(root, text=name[i])
    name_label.grid(row=i+1, column=0)

    age_label = Label(root, text=age[i])
    age_label.grid(row=i+1, column=1)

root.mainloop()