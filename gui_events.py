import tkinter as tk
from tkinter import ttk
import customtkinter as ct
from func_utils import *
from Events import event_manager
from student import student_manager


# Using EventController in order to separate logic from the view. Easier to scale up and debug this way. Later on,
# we might just make one controller for both Events and Students or make a MetaController that is a parent of both
class EventController:
    def __init__(self, view):
        # view = EventsFrame() getting student_controller, we need to make a way for event controller to access the
        # student manager that is created in gui_students. for now I will create my own for testing
        self.student_model = student_manager
        # defining the view and model. view is EventFrame passed into Controller later on.
        # Model is the EventManger
        self.view = view
        self.model = event_manager

        self.events_table = self.view.date_table
        self.event_tabs = self.view.event_tabs

        # Functions run Initially
        self.update_events_table()
        self.widget_bindings()

    # adds to model, deletes and repopulates items in view using update_events_table
    def add_event(self, event=None):
        add_tab = self.event_tabs.add_tab
        validation = self.validate_add_edit_tab(add_tab)
        if validation == True:
            self.model.add_event(int(add_tab.id.var.get()), add_tab.name.var.get(), add_tab.date.var.get(),
                                 add_tab.nature.var.get(), add_tab.description.get('0.0', 'end'))
            self.update_events_table()
        else:
            error_string = ''
            for error in validation:
                error_string += '\n' + error
            tk.messagebox.showerror("showerror", "There were errors in data entry: " + error_string)

    # deletes an event in model, deletes and repopulates items in view update_events_table
    def delete_event(self, event=None):
        item = self.events_table.tree.focus()
        if item:
            self.model.delete_event(item)
            self.update_events_table()
        else:
            raise Exception("No Event selected")

    # Edits a selected event and updates treeview
    def edit_event(self, event=None):
        edit_tab = self.event_tabs.edit_tab
        selected_item = self.events_table.tree.focus()
        validation = self.validate_add_edit_tab(edit_tab, selected_item)
        if validation == True:
            event = self.model.get_event(selected_item)
            event.event_id = int(edit_tab.id.var.get())
            event.name = edit_tab.name.var.get()
            event.date = edit_tab.date.var.get()
            event.nature = edit_tab.nature.var.get()
            event.event_description = edit_tab.description.get('0.0', 'end')
            self.update_events_table()
        else:
            error_string = ''
            for error in validation:
                error_string += '\n' + error
            tk.messagebox.showerror("showerror", "There were errors in data entry: " + error_string)

    # callback to when a row is double clicked, populates the edit tab entries.
    def edit_select_fill(self, event=None):
        selected_item = self.events_table.tree.focus()
        edit_tab = self.event_tabs.edit_tab
        event = self.model.get_event(selected_item)
        # check if the edit_tab is at the top of display stack by checking if it is placed last:
        if edit_tab == self.event_tabs.winfo_children()[-1]:
            edit_tab.id.var.set(event.event_id)
            edit_tab.name.var.set(event.name)
            edit_tab.date.var.set(event.date)
            edit_tab.nature.var.set(event.nature)
            edit_tab.description.delete('0.0', 'end')
            edit_tab.description.insert('end', event.event_description)

    def view_select(self, event=None):
        selected_item = self.events_table.tree.focus()
        view_tab = self.event_tabs.view_tab
        event = self.model.get_event(selected_item)
        if event:
            if view_tab == self.event_tabs.winfo_children()[-1]:
                attendee_names = [f'{student_ref().first_name} {student_ref().last_name}, {student_ref().student_id}'
                                  for student_ref in event.attendees if student_ref()]
                view_tab.event_name.var.set(event.name)
                view_tab.description.delete("0.0", 'end')
                view_tab.description.insert('end', event.event_description)
                view_tab.student_list.var.set(attendee_names)

    def add_student_view(self, event=None):
        selected_item = self.events_table.tree.focus()
        student_id = self.event_tabs.view_tab.student_select.var.get().split()[2]
        student = self.student_model.get_student(int(student_id))
        event = self.model.get_event(selected_item)
        validation = self.validate_view_tab_add(student)
        if validation == True:
            event.add_attendee(student)
            self.update_view_tab()
        else:
            error_string = ''
            for error in validation:
                error_string += '\n' + error
            tk.messagebox.showerror("showerror", "There were errors in data entry: " + error_string)

    def delete_student_view(self, event=None):
        indexes = self.event_tabs.view_tab.student_list.curselection()
        event = self.model.get_event(self.events_table.tree.focus())
        validation = self.validate_view_tab_delete(indexes)
        if validation == True:
            attendees = event.attendees
            for idx in indexes:
                event.delete_attendee(attendees[idx])
            self.update_view_tab()
        else:
            error_string = ''
            for error in validation:
                error_string += '\n' + error
            tk.messagebox.showerror("showerror", "There were errors in data entry: " + error_string)

    # Validation functions
    def validate_add_edit_tab(self, tab, selected_item=None):
        data_entries = [tab.id.var.get(), tab.name.var.get(), tab.date.var.get(), tab.nature.var.get()]
        errors = []
        event = None
        if selected_item:
            event = self.model.get_event(selected_item)
        elif tab == self.event_tabs.edit_tab:
            errors.append('\tNo Event is selected')

        errors.append(self.model.validate_id(data_entries[0], event))
        errors.append(self.model.validate_event_name(data_entries[1]))
        errors.append(self.model.validate_date(data_entries[2]))
        errors.append(self.model.validate_nature(data_entries[3]))

        errors = [error for error in errors if not isinstance(error, bool)]
        return errors if errors else True

    def validate_view_tab_add(self, student):
        errors = []
        selected_item = self.events_table.tree.focus()
        event = self.model.get_event(selected_item)
        if not selected_item:
            errors.append('\tNo Event is selected')
        elif student in [s() for s in event.attendees if s]:
            errors.append('\tStudent already attended event')

        return errors if errors else True

    def validate_view_tab_delete(self, idexes):
        errors = []
        selected_item = self.events_table.tree.focus()
        event = self.model.get_event(selected_item)
        if not selected_item:
            errors.append('\tNo Event is selected')
        elif not idexes:
            errors.append('\tNo Student is selected')

        return errors if errors else True

    # Updates and bindings
    # updates the treeview each time it is called. Call it anytime the model is changed.
    # It deletes all items from treeview and repopulates them
    def update_events_table(self):
        self.events_table.tree.delete(*self.events_table.tree.get_children())
        self.events_table.load_events(self.model.events)

    def update_view_tab(self):
        values = [f'{s.first_name} {s.last_name}, {s.student_id}' for s in self.student_model.students]
        self.event_tabs.view_tab.student_select.configure(values=values)
        self.event_tabs.view_tab.student_select.var.set(value=values[0])
        #self.view_select()
        selected_item = self.events_table.tree.focus()
        view_tab = self.event_tabs.view_tab
        event = self.model.get_event(selected_item)
        if not event:
            item = self.events_table.tree.get_children()[0]
            event = self.model.get_event(item)
        attendee_names = [f'{student_ref().first_name} {student_ref().last_name}, {student_ref().student_id}'
                          for student_ref in event.attendees if student_ref()]
        view_tab.event_name.var.set(event.name)
        view_tab.description.delete("0.0", 'end')
        view_tab.description.insert('end', event.event_description)
        view_tab.student_list.var.set(attendee_names)

    # All bindings and command configs to widgets are done here
    def widget_bindings(self):
        self.events_table.tree.bind('<Double-1>', self.edit_select_fill)
        self.events_table.tree.bind('<ButtonRelease-1>', self.view_select)
        self.event_tabs.add_tab.add.configure(command=self.add_event)
        self.event_tabs.add_tab.delete.configure(command=self.delete_event)

        self.event_tabs.edit_tab.edit_button.configure(command=self.edit_event)

        self.event_tabs.view_tab.student_add.configure(command=self.add_student_view)
        self.event_tabs.view_tab.delete_student.configure(command=self.delete_student_view)

        values = [f'{s.first_name} {s.last_name}, {s.student_id}' for s in self.student_model.students]
        self.event_tabs.view_tab.student_select.configure(values=values)
        self.event_tabs.view_tab.student_select.var.set(value=values[0])


# Combining both frames
class EventsFrame(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(fg_color="transparent")

        # Making the layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=10)
        self.columnconfigure(1, weight=1)

        # Making Data Table and loading data
        self.date_table = EventsTable(self)
        self.date_table.grid(row=0, column=0, sticky='NSEW', padx=10, pady=30)
        # em = EventManager()
        # self.date_table.load_events(em.events)

        # The various tabs
        self.event_tabs = EventTools(self)
        self.event_tabs.grid(row=0, column=1, sticky='NSEW', padx=10, pady=30)

        # Fixing all placeholders for all entries that is a child of this widget.
        place_holder_bind_all(self)


# DataTable displaying events
class EventsTable(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Setting Style
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Treeview', fieldbackground='#343638', rowheight=40)
        s.configure('Treeview.Heading',
                    background="#343638", foreground='gray',
                    font=('Helvetica', 20, 'bold'), fieldbackground='#343638')

        # Initializing treeview, and scroller
        self.tree = ttk.Treeview(self)
        self.scroll_y = ct.CTkScrollbar(self, orientation="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll_y.set)

        self.scroll_x = ct.CTkScrollbar(self, orientation="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.scroll_x.set)

        # Griding in the table and scroller
        self.tree.grid(row=0, column=0, sticky='NSEW')
        self.scroll_y.grid(row=0, column=1, sticky='NSEW')
        self.scroll_x.grid(row=1, column=0, sticky='NSEW')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Setting up columns
        self.tree.heading("#0", text='ID', )
        self.tree.column("#0", width=200, anchor='center', minwidth=200)
        columns = ("Event Name", 'Date', 'Nature')
        self.tree["columns"] = columns
        for column in columns:
            self.tree.heading(column, text=column)
            if column == 'Event Name':
                self.tree.column(column, width=300, anchor='center', minwidth=300)
            else:
                self.tree.column(column, width=200, anchor='center', minwidth=200)

    # loads Events to treeview. called in EventController
    def load_events(self, events):
        for event in events:
            values = (event.name, event.date, event.nature)
            event_id = str(event.event_id)
            self.tree.insert("", 'end', event_id, text=event_id, values=values, tags=('ttk', 'simple', 'events'))
            self.tree.tag_configure('ttk', font=('Helvetica', 20, 'bold'), foreground='gray74', background='#343638')


class EventTools(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Grid layout:
        self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)

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
        self.nav_frame.configure(fg_color="transparent")

        # Nav_frame layout:
        self.nav_frame.columnconfigure(0, weight=1)
        self.nav_frame.columnconfigure(1, weight=1)
        self.nav_frame.columnconfigure(2, weight=1)

        # Nav buttons
        font = ('arial', 16, 'bold')
        border_width = 2
        border_color = ("#3B8ED0", "#1F6AA5")
        corner_radius = 5
        fg_color = ("#3B8ED0", "#1F6AA5")
        text_color = ("#DCE4EE", "#DCE4EE")
        hover_color = ('#325882', '#14375e')
        height = 40
        anchor = "center"

        nav_add = ct.CTkButton(self.nav_frame, text="Add tab", command=lambda: self.show_frame(AddTab, nav_add),
                               border_width=border_width, border_color=border_color, corner_radius=corner_radius,
                               fg_color=fg_color, text_color=text_color, font=font,
                               hover_color=hover_color, height=height,
                               anchor=anchor, )
        nav_add.grid(row=0, column=0, sticky='NEWS')

        nav_del = ct.CTkButton(self.nav_frame, text="Edit tab", command=lambda: self.show_frame(EditTab, nav_del),
                               border_width=border_width, border_color=border_color, corner_radius=corner_radius,
                               fg_color=fg_color, text_color=text_color, font=font,
                               hover_color=hover_color, height=height,
                               anchor=anchor, )
        nav_del.grid(row=0, column=1, sticky='NEWS')

        nav_view = ct.CTkButton(self.nav_frame, text="View tab", command=lambda: self.show_frame(ViewTab, nav_view),
                                border_width=border_width, border_color=border_color, corner_radius=corner_radius,
                                fg_color=fg_color, text_color=text_color, font=font,
                                hover_color=hover_color, height=height,
                                anchor=anchor, )
        nav_view.grid(row=0, column=2, sticky='NEWS')

        self.show_frame(AddTab, nav_add)

        # Add tabs to self
        self.add_tab = self.frames[AddTab]
        self.edit_tab = self.frames[EditTab]
        self.view_tab = self.frames[ViewTab]

    def show_frame(self, cont, button=None):
        if button:
            for child in self.nav_frame.winfo_children():
                child.configure(fg_color=("#3B8ED0", "#1F6AA5"))
            button.configure(fg_color=('#F9F9FA', '#343638'))

        frame = self.frames[cont]
        frame.tkraise()


class AddTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(fg_color="transparent")
        # Creating widgets
        font = 20
        self.name = ct.CTkEntry(self, placeholder_text='Event Name', font=('arial', font))
        self.date = ct.CTkEntry(self, placeholder_text='Date', font=('arial', font))
        # use IntVar
        self.id = ct.CTkEntry(self, placeholder_text='ID', font=('arial', font))
        self.nature = ct.CTkEntry(self, placeholder_text='Nature', font=('arial', font))
        self.description = ct.CTkTextbox(self, height=100, font=('arial', font))
        self.add = ct.CTkButton(self, text="Add Event", font=('arial', font))
        self.delete = ct.CTkButton(self, text="Delete Event", font=('arial', font))

        # add_default text for description box
        self.description.insert('0.0', 'Description of the event')
        # griding in entries
        pad = 10
        self.name.grid(row=0, column=0, sticky='NEWS', padx=pad, pady=(pad + 30, pad))
        self.date.grid(row=0, column=1, sticky='NEWS', padx=pad, pady=(pad + 30, pad))
        self.id.grid(row=1, column=0, sticky='NEWS', padx=pad, pady=pad + 10)
        self.nature.grid(row=1, column=1, sticky='NEWS', padx=pad, pady=pad + 10)
        self.description.grid(row=2, sticky='NEWS', padx=pad, pady=pad, columnspan=2)
        self.add.grid(row=3, sticky='NEWS', padx=pad, pady=pad, columnspan=2)
        self.delete.grid(row=4, sticky='NEWS', padx=pad, pady=pad, columnspan=2)

        # applying a weight of 1 to all cells
        limited_weight_cells(self)
        # add vars to all entries
        self.add_vars_to_entries()

    def add_vars_to_entries(self):
        self.name.var = tk.StringVar()
        self.name.configure(textvariable=self.name.var)
        self.date.var = tk.StringVar()
        self.date.configure(textvariable=self.date.var)
        self.id.var = tk.StringVar()
        self.id.configure(textvariable=self.id.var)
        self.nature.var = tk.StringVar()
        self.nature.configure(textvariable=self.nature.var)


class EditTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(fg_color="transparent")
        # Creating widgets
        font = 20
        self.name = ct.CTkEntry(self, placeholder_text='Event Name', font=('arial', font))
        self.date = ct.CTkEntry(self, placeholder_text='Date', font=('arial', font))
        # Use IntVar
        self.id = ct.CTkEntry(self, placeholder_text='ID', font=('arial', font))
        self.nature = ct.CTkEntry(self, placeholder_text='Nature', font=('arial', font))
        self.description = ct.CTkTextbox(self, height=100, font=('arial', font))
        self.edit_button = ct.CTkButton(self, text="Edit Event", font=('arial', font), anchor='center')

        # add_default text for description box
        self.description.insert('0.0', 'Description of the event')

        # griding in entries
        pad = 10
        self.name.grid(row=0, column=0, sticky='NEWS', padx=pad, pady=(pad + 30, pad))
        self.date.grid(row=0, column=1, sticky='NEWS', padx=pad, pady=(pad + 30, pad))
        self.id.grid(row=1, column=0, sticky='NEWS', padx=pad, pady=pad + 10)
        self.nature.grid(row=1, column=1, sticky='NEWS', padx=pad, pady=pad + 10)
        self.description.grid(row=2, sticky='NEWS', padx=pad, pady=pad, columnspan=2)
        self.edit_button.grid(row=3, sticky='NEWS', padx=pad + 40, pady=pad, columnspan=2)
        # applying a weight of 1 to all cells
        limited_weight_cells(self)

        # Evening out the different tab alignment
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        # add vars to all entries
        self.add_vars_to_entries()

    def add_vars_to_entries(self):
        self.name.var = tk.StringVar()
        self.name.configure(textvariable=self.name.var)
        self.date.var = tk.StringVar()
        self.date.configure(textvariable=self.date.var)
        self.id.var = tk.StringVar()
        self.id.configure(textvariable=self.id.var)
        self.nature.var = tk.StringVar()
        self.nature.configure(textvariable=self.nature.var)


class ViewTab(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(fg_color="transparent")
        self.event_name = ct.CTkLabel(self, text="Event Name", font=('arial', 30))
        # Student_list
        self.student_list = tk.Listbox(self, height=3, borderwidth=10,
                                       width=15, background="#343638", activestyle='dotbox',
                                       font=("Helvetica", 15, "bold"), foreground="gray"
                                       )
        # student tools
        self.student_tools = ct.CTkFrame(self, fg_color='transparent')
        self.student_select = ct.CTkComboBox(self.student_tools)
        self.student_add = ct.CTkButton(self.student_tools, text='Add Student', font=('arial', 20), anchor='center')
        self.delete_student = ct.CTkButton(self.student_tools, text='Delete Student', font=('arial', 20),
                                           anchor='center')

        self.description = ct.CTkTextbox(self, height=200, font=('arial', 20))
        # add_default text for description box
        self.description.insert('0.0', 'Description of the event')

        # griding
        pad = 10
        self.event_name.grid(row=0, column=0, sticky='NSEW', columnspan=2,
                             padx=pad + 40, pady=(pad + 20, pad + 10))
        self.student_list.grid(row=1, column=0, sticky='NSEW', padx=(pad, 0), pady=pad, rowspan=3)

        self.student_tools.grid(row=1, column=1, sticky='NSEW', padx=0, pady=pad)
        self.student_select.grid(row=0, column=0, sticky='NSEW', padx=pad, pady=0)
        self.student_add.grid(row=1, column=0, sticky='NSEW', padx=pad, pady=pad)
        self.delete_student.grid(row=2, column=0, sticky='NSEW', padx=pad, pady=0)

        self.description.grid(row=4, column=0, sticky='NSEW', padx=pad, pady=pad, columnspan=2)

        # applying a weight of 1 to all cells
        limited_weight_cells(self)

        # Manually editing layout
        self.rowconfigure(4, weight=7)

        # add vars to all applicable widgets
        self.add_vars()

    def add_vars(self):
        self.event_name.var = tk.StringVar(value="Event Name")
        self.event_name.configure(textvariable=self.event_name.var)
        self.student_list.var = tk.StringVar(value=[])
        self.student_list.configure(listvariable=self.student_list.var)
        self.student_select.var = tk.StringVar()
        self.student_select.configure(variable=self.student_select.var)


if __name__ == "__main__":
    window = ct.CTk()
    # Setting size of the window
    # window.geometry("1300x550")
    ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ct.set_default_color_theme("dark-blue")

    E = EventsFrame(window)
    E.grid(row=0, column=0, sticky='NSEW')
    # EventTools(window).grid(row=0, column=0, sticky='NSEW')
    # EventsTable(window).grid(row=0, column=0, sticky='NSEW')

    # AddTab(window).grid(row=0, column=0, sticky='NSEW')

    # Running controller
    controller = EventController(E)

    # Making the widgets resizable
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    window.mainloop()
