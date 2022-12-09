from tkinter import *
from tkinter.ttk import Treeview

root = Tk()

# Create a Treeview widget
tree = Treeview(root)

# Create a vertical scrollbar
vsb = Scrollbar(root, orient ="vertical", command = tree.yview)

# Attach the scrollbar to the Treeview
tree.configure(yscrollcommand = vsb.set)

# Add items to the Treeview
tree.insert("" , 1, "item1", text ="This is item 1")
tree.insert("" , 2, "item2", text ="This is item 2")

# Pack the Treeview and the Scrollbar
tree.pack(side ="left")
vsb.pack(side ="right", fill ="y")

# Add additional items
for i in range(50):
    tree.insert("", "end", text=f"Item {i}")

root.mainloop()