import customtkinter
import customtkinter as ct
from PIL import Image
from gui_events import *
from gui_report import *
from gui_home import HomeFrame, HomeController
import gui_students as s2
import gui_help


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1400x600")
        self.title("Attendance Tracker")
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")
        NavigationFrameTop(self).grid(padx=0, pady=0, row=0, column=0, sticky="NEWS")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


# For example Purposes
class Login(ct.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.configure(fg_color="transparent")
        main_frame = ct.CTkFrame(self)
        main_frame.grid(row=0, column=0, )

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        ct.CTkLabel(main_frame, text='Login Screen', font=("arial", 30)).grid(row=0, column=0, sticky="NSEW", pady=12,
                                                                              padx=10)
        username = ct.CTkEntry(main_frame, placeholder_text='Username', font=("arial", 25))
        username.grid(row=1, column=0, sticky="NSEW", pady=12, padx=30)
        password = ct.CTkEntry(main_frame, placeholder_text='Password', font=("arial", 25))
        password.grid(row=2, column=0, sticky="NSEW", pady=12, padx=30)
        remember_me_box = ct.CTkCheckBox(main_frame, text='Remember me')
        remember_me_box.grid(row=3, column=0, sticky="NSEW", pady=12, padx=40)
        btn_login = ct.CTkButton(main_frame, text='Login')
        btn_login.grid(row=4, column=0, sticky="NSEW", pady=12, padx=30)

        for child in main_frame.winfo_children():
            main_frame.rowconfigure(child.grid_info()['row'], weight=1, minsize=100)
            main_frame.columnconfigure(child.grid_info()['column'], weight=1, minsize=500)


# Nav bar at the top, Alternate view. Access by changing 'NavigationFrame' to 'NavigationFrameTop' in the App class.
class NavigationFrameTop(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(fg_color="transparent")
        # set grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=15)
        self.grid_columnconfigure(0, weight=1)
        # images & Icons
        self.home_image = ct.CTkImage(Image.open("images/home_light.png"), size=(26, 26))
        self.student_image = ct.CTkImage(Image.open("images/students_light.png"), size=(26, 26))
        self.event_image = ct.CTkImage(Image.open("images/events_light.png"), size=(26, 26))
        self.report_image = ct.CTkImage(Image.open("images/report_light.png"), size=(26, 26))
        self.help_image = ct.CTkImage(Image.open("images/help_light.png"), size=(26, 26))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=10, fg_color='#343638')
        self.navigation_frame.grid(row=0, column=0, sticky="new")
        self.navigation_frame.columnconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Navigation",
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Buttons to navigate
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home", image=self.home_image,
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=0, column=1, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Students", image=self.student_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=0, column=2, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Events", image=self.event_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=0, column=3, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Report", image=self.report_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=0, column=4, sticky="ew")

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Help", image=self.help_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=0, column=5, sticky="ew")

        for child in self.navigation_frame.winfo_children():
            self.navigation_frame.rowconfigure(child.grid_info()['row'], weight=1)
            # self.navigation_frame.columnconfigure(child.grid_info()['column'], weight=1)

        # Appearance changer
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        # self.appearance_mode_menu.grid(row=0, column=6, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = HomeFrame(self)
        self.HC = HomeController(self.home_frame)

        # create second frame
        self.second_frame = s2.StudentsFrame(self)
        self.SC = s2.StudentController(self.second_frame)

        # create third frame
        self.third_frame = EventsFrame(self)
        self.EC = EventController(self.third_frame)

        # create fourth frame
        self.fourth_frame = ReportFrame(self)
        self.RC = ReportController(self.fourth_frame)

        # create fifth Frame
        self.fifth_frame = gui_help.HelpMenu(self)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        self.cross_frame_func()
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "frame_5":
            self.fifth_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # function that must be syncronized across frames. run whenever a frame is changed
    def cross_frame_func(self):
        self.SC.update_students_table()

        self.EC.update_events_table()
        self.EC.update_view_tab()

        self.RC.update_table()
        self.RC.update_display()

        self.HC.update()


# Nav bar at the top, Default view. Access by changing 'NavigationFrameTop' to 'NavigationFrame' in the App class.
class NavigationFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(fg_color="transparent")
        # set grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=15)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=10, fg_color='#343638')
        self.navigation_frame.grid(row=0, column=0, sticky="nws")
        self.navigation_frame.rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Navigation",
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # images & Icons
        self.home_image = ct.CTkImage(Image.open("images/home_light.png"), size=(26, 26))
        self.student_image = ct.CTkImage(Image.open("images/students_light.png"), size=(26, 26))
        self.event_image = ct.CTkImage(Image.open("images/events_light.png"), size=(26, 26))
        self.report_image = ct.CTkImage(Image.open("images/report_light.png"), size=(26, 26))
        self.help_image = ct.CTkImage(Image.open("images/help_light.png"), size=(26, 26))


        # Buttons to navigate
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home", image=self.home_image,
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Students", image=self.student_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Events", image=self.event_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Report", image=self.report_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Help", image=self.help_image,
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

        for child in self.navigation_frame.winfo_children():
            # self.navigation_frame.rowconfigure(child.grid_info()['row'], weight=1)
            self.navigation_frame.columnconfigure(child.grid_info()['column'], weight=1)

        # Appearance changer
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        # self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = HomeFrame(self, fg_color='transparent')
        self.HC = HomeController(self.home_frame)

        # create second frame
        self.second_frame = s2.StudentsFrame(self, fg_color='transparent')
        self.SC = s2.StudentController(self.second_frame)

        # create third frame
        self.third_frame = EventsFrame(self, fg_color='transparent')
        self.EC = EventController(self.third_frame)

        # create fourth frame
        self.fourth_frame = ReportFrame(self, fg_color='transparent')
        self.RC = ReportController(self.fourth_frame)

        # create fifth Frame
        self.fifth_frame = gui_help.HelpMenu(self, fg_color='transparent')

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        self.cross_frame_func()
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "frame_5":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # function that must be syncronized across frames. run whenever a frame is changed
    def cross_frame_func(self):
        self.SC.update_students_table()

        self.EC.update_events_table()
        self.EC.update_view_tab()

        self.RC.update_table()
        self.RC.update_display()

        self.HC.update()


if __name__ == "__main__":
    app = App()
    app.mainloop()
