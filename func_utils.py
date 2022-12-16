# A function to add weight to all widget:
def weight_cells_1(parent):
    for child in parent.winfo_children():

        if "row" in child.grid_info() and 'column' in child.grid_info():
            parent.rowconfigure(child.grid_info()['row'], weight=1)
            parent.columnconfigure(child.grid_info()['column'], weight=1)
            if child.grid_info():
                weight_cells_1(child)