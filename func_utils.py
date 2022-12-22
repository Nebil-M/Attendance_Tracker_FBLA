import customtkinter as ct


# A function to add a weight of 1 to ALL child widgets inside the parent
# Might mess with anchoring of text inside buttons
def weight_cells_1(parent):
    for child in parent.winfo_children():
        if "row" in child.grid_info() and 'column' in child.grid_info():
            parent.rowconfigure(child.grid_info()['row'], weight=1)
            parent.columnconfigure(child.grid_info()['column'], weight=1)
            if child.grid_info():
                weight_cells_1(child)


# Assigns a weight of one to all child widgets inside the parent except buttons:
def limited_weight_cells(parent):
    for child in parent.winfo_children():
        if "row" in child.grid_info() and 'column' in child.grid_info():
            parent.rowconfigure(child.grid_info()['row'], weight=1)
            parent.columnconfigure(child.grid_info()['column'], weight=1)
            if child.grid_info() and not isinstance(child, ct.windows.widgets.ctk_button.CTkButton):
                limited_weight_cells(child)


## Placeholder text with control variable

# helper func for placeholder functions
def entry_focus(widget):
    if widget.get() == widget.cget('placeholder_text'):
        widget.delete('0', 'end')
        widget.configure(text_color=('gray14', 'gray84'))

# helper func for placeholder functions
def entry_unfocus(widget):
    if not widget.get():
        widget.insert('end', widget.cget('placeholder_text'))
        widget.configure(text_color=('gray52', 'gray62'))

# Makes placeholder work for all widgets inside a parent Unless max depth is specified.
def place_holder_bind_all(parent, max_depth=9 ** 9, depth=0):
    for child in parent.winfo_children():
        place_holder_bind_widget(child)
        if max_depth > depth:
            place_holder_bind_all(child, depth=depth + 1)

# makes placeholder work for a single widget.
def place_holder_bind_widget(widget):
    if isinstance(widget, ct.windows.widgets.ctk_entry.CTkEntry) and widget.cget("placeholder_text"):
        if not widget.get():
            widget.insert('end', widget.cget('placeholder_text'))
        widget.configure(text_color=('gray52', 'gray62'))
        widget.bind('<FocusIn>', lambda e: entry_focus(widget))
        widget.bind('<FocusOut>', lambda e: entry_unfocus(widget))
