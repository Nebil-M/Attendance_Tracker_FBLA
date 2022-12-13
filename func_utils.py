# A function to add weight to all widget:
def weight_cells_1(parent):
    for child in parent.winfo_children():
        parent.rowconfigure(child.grid_info()['row'], weight=1)
        parent.columnconfigure(child.grid_info()['column'], weight=1)
        if child.grid_info():
            weight_cells_1(child)