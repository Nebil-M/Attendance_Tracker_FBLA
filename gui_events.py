import tkinter as tk
from tkinter import ttk
import customtkinter as ct
from func_utils import weight_cells_1
from Events import EventManager


# Combining both frames
class EventsFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        table = EventsTable(self)
        em = EventManager()
        table.load_events(em.events)
        table.grid(row=0, column=0, sticky='NSEW', padx=30, pady=30)

        EventTools(self).grid(row=0, column=1, sticky='NSEW')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)


class EventsTable(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initializing and setting size
        self.tree = ttk.Treeview(self)
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scroll.set)

        # Gridding in the table and scroller
        self.tree.grid(row=0, column=0, sticky='NSEW')
        self.scroll.grid(row=0, column=1, sticky='NSEW')
        # self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Setting up columns
        self.tree.heading("#0", text='ID', )
        self.tree.column("#0", width=100, anchor='center')
        columns = ("Event Name", 'Date', 'Nature', "Description")
        self.tree["columns"] = columns
        for column in columns:
            self.tree.heading(column, text=column, )
            self.tree.column(column, width=100, anchor='center')

    def add_event(self, event):
        values = (event.name, event.date, event.is_sport, event.event_description)
        event_id = str(event.event_id)
        self.tree.insert("", 'end', event_id, text=event_id, values=values)

    def load_events(self, events):
        for event in events:
            values = (event.name, event.date, event.nature, event.event_description)
            event_id = str(event.event_id)
            self.tree.insert("", 'end', event_id, text=event_id, values=values, tags=('ttk', 'simple'))
            self.tree.tag_configure('ttk', background='lightGray', font=('Helvetica', 12))


class EventTools(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        self.tabs = [AddTab, EditTab, ViewTab]
        for F in self.tabs:
            frame = F(self)
            # initializing frame of each Frame
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky="NEWS", columnspan=5)
            self.columnconfigure(0, weight=1)
            self.rowconfigure(1, weight=1)

        # Nav frame
        self.nav_frame = ct.CTkFrame(self)
        self.nav_frame.grid(row=0, column=0, sticky='NWS')
        self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)

        # Nav buttons
        nav_add = ct.CTkButton(self.nav_frame, text="Add tab", command=lambda: self.show_frame(AddTab, nav_add),
                               border_width=4, border_color=("#3B8ED0", "#1F6AA5"), corner_radius=20,
                               fg_color=("#3B8ED0", "#1F6AA5"), text_color=("#DCE4EE", "#DCE4EE"),
                               hover_color=("#3E454A", "#949A9F"), height=40,
                               anchor="w", )
        nav_add.grid(row=0, column=0, sticky='NEWS')
        self.nav_frame.columnconfigure(0, weight=1)

        nav_del = ct.CTkButton(self.nav_frame, text="del tab", command=lambda: self.show_frame(EditTab, nav_del),
                               border_width=4, border_color=("#3B8ED0", "#1F6AA5"), corner_radius=20,
                               fg_color=("#3B8ED0", "#1F6AA5"), text_color=("#DCE4EE", "#DCE4EE"),
                               hover_color=("#3E454A", "#949A9F"), height=40,
                               anchor="w", )
        nav_del.grid(row=0, column=1, sticky='NEWS')
        self.nav_frame.columnconfigure(1, weight=1)
        nav_view = ct.CTkButton(self.nav_frame, text="del tab", command=lambda: self.show_frame(ViewTab, nav_view),
                               border_width=4, border_color=("#3B8ED0", "#1F6AA5"), corner_radius=20,
                               fg_color=("#3B8ED0", "#1F6AA5"), text_color=("#DCE4EE", "#DCE4EE"),
                               hover_color=("#3E454A", "#949A9F"), height=40,
                               anchor="w", )

        nav_view.grid(row=0, column=2, sticky='NEWS')
        self.nav_frame.columnconfigure(1, weight=1)


        self.show_frame(AddTab, nav_add)

    def show_frame(self, cont, button=None):
        if button:
            for child in self.nav_frame.winfo_children():
                child.configure(fg_color=("#3B8ED0", "#1F6AA5"))
            button.configure(fg_color=("#3E454A", "#949A9F"))
        frame = self.frames[cont]
        frame.tkraise()


class AddTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ct.CTkButton(self, text='ADD').grid(column=0, row=0, sticky='NSEW', padx=20, pady=20)
        # Creating widgets
        font = 20
        self.name = ct.CTkEntry(self, placeholder_text='Event Name', font=('arial', font))
        self.date = ct.CTkEntry(self, placeholder_text='Date', font=('arial', font))
        self.id = ct.CTkEntry(self, placeholder_text='ID', font=('arial', font))
        self.nature = ct.CTkEntry(self, placeholder_text='nature', font=('arial', font))
        self.description = ct.CTkTextbox(self, height=100, font=('arial', font))
        self.add = ct.CTkButton(self, text="Add", font=('arial', font))
        self.delete = ct.CTkButton(self, text="Delete", font=('arial', font))

        # add_default text for description box
        self.description.insert('0.0', 'Description of the event')
        # griding in entries
        pad = 10
        self.name.grid(row=0, column=0, sticky='NEWS', padx=pad, pady=pad + 30)
        self.date.grid(row=0, column=1, sticky='NEWS', padx=pad, pady=pad + 30)
        self.id.grid(row=1, column=0, sticky='NEWS', padx=pad, pady=pad + 10)
        self.nature.grid(row=1, column=1, sticky='NEWS', padx=pad, pady=pad + 10)
        self.description.grid(row=2, sticky='NEWS', padx=pad, pady=pad, columnspan=2)
        self.add.grid(row=3, sticky='NEWS', padx=pad, pady=pad, columnspan=2)
        self.delete.grid(row=4, sticky='NEWS', padx=pad, pady=pad, columnspan=2)
        #

        weight_cells_1(self)


class EditTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Creating widgets
        font = 20
        self.name = ct.CTkEntry(self, placeholder_text='Event Name', font=('arial', font))
        self.date = ct.CTkEntry(self, placeholder_text='Date', font=('arial', font))
        self.id = ct.CTkEntry(self, placeholder_text='ID', font=('arial', font))
        self.nature = ct.CTkEntry(self, placeholder_text='nature', font=('arial', font))
        self.description = ct.CTkTextbox(self, height=100, font=('arial', font))
        self.edit_button = ct.CTkButton(self, text="Edit", font=('arial', font), anchor='center')

        # add_default text for description box
        self.description.insert('0.0', 'Description of the event')

        # griding in entries
        pad = 10
        self.name.grid(row=0, column=0, sticky='NEWS', padx=pad, pady=pad + 30)
        self.date.grid(row=0, column=1, sticky='NEWS', padx=pad, pady=pad + 30)
        self.id.grid(row=1, column=0, sticky='NEWS', padx=pad, pady=pad + 10)
        self.nature.grid(row=1, column=1, sticky='NEWS', padx=pad, pady=pad + 10)
        self.description.grid(row=2, sticky='NEWS', padx=pad, pady=pad, columnspan=2)
        self.edit_button.grid(row=3, sticky='NEWS', padx=pad+40, pady=pad, columnspan=2)
        # applying a weight of 1 to all cells
        weight_cells_1(self)


class ViewTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = ct.CTkEntry(self, placeholder_text="Event ID", font=('arial', 20), height=5)
        self.id_enter = ct.CTkButton(self, text="Confirm", font=('arial', 40), height=5)
        # Student_list
        self.student_list = ct.CTkFrame(self, border_width=4, border_color='black', height=100)
        self.description = ct.CTkTextbox(self, height=200, font=('arial', 20))

        # gridding
        pad = 10
        self.id.grid(row=0, column=0, sticky='NSEW', padx=(pad+90, pad+10), pady=(pad+40, pad+10))
        self.id_enter.grid(row=0, column=1, sticky='NSEW', padx=(pad+10, pad+90), pady=(pad+40, pad+10))

        self.student_list.grid(row=1, column=0, sticky='NSEW', padx=pad+40, pady=pad, columnspan=2)
        self.description.grid(row=2, column=0, sticky='NSEW', padx=pad+40, pady=pad, columnspan=2)

        # applying a weight of 1 to all cells
        weight_cells_1(self)


if __name__ == "__main__":
    window = ct.CTk()
    # Setting size of the window
    window.geometry("1300x550")
    ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ct.set_default_color_theme("dark-blue")

    #EventsFrame(window).grid(row=0, column=0, sticky='NSEW')
    # EventTools(window).grid(row=0, column=0, sticky='NSEW')
    # EventsTable(window).grid(row=0, column=0, sticky='NSEW')

    ViewTab(window).grid(row=0, column=0, sticky='NSEW')

    # Making the widgets resizable
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
