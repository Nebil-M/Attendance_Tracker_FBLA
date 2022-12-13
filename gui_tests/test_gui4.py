import tkinter as tk
from tkinter import ttk

class TreeviewTable(ttk.Frame):
    def __init__(self, parent, columns, height=5):
        # Initialize the parent class
        ttk.Frame.__init__(self, parent)

        # Create the treeview widget
        self.treeview = ttk.Treeview(self, height=height)

        # Create a vertical scrollbar for the treeview
        ysb = ttk.Scrollbar(self, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscroll=ysb.set)

        # Define the columns for the treeview
        self.treeview["columns"] = columns

        # Set the column headings
        for col in columns:
            self.treeview.heading(col, text=col.title())

        # Set the text for the first column heading
        self.treeview.heading("#0", text="Item")

        # Hide the default "Item" column, if it exists
        if self.treeview.exists("#0"):
            self.treeview.column("#0", show="none")

        # Add the treeview and scrollbar to the frame
        self.treeview.grid(row=0, column=0, sticky="nsew")
        ysb.grid(row=0, column=1, sticky="ns")

        # Set the column and row weights
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def add_data(self, parent, data):
        # Add data to the treeview
        for item in data:
            self.treeview.insert(parent, "end", text='P', values=item)

# Create the root window
root = tk.Tk()

# Create an instance of the TreeviewTable class
table = TreeviewTable(root, columns=("one", "two", "three"))

# Add the treeview table to the root window at row 0, column 0
table.grid(row=0, column=0)

# Add some data to the table
data1 = (("1A", "1B", "1C"),
         ("2A", "2B", "2C"),
         ("3A", "3B", "3C"))
table.add_data("", data1)

data2 = (("4A", "4B", "4C"),
         ("5A", "5B", "5C"),
         ("6A", "6B", "6C"))
table.add_data("", data2)

# Run the main event loop
root.mainloop()
