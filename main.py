import customtkinter
import customtkinter as ct


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.title("Main")
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")
        NavigationFrame(self).grid(padx=0, pady=0, row=0, column=0)


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
        btn_login = ct.CTkButton(main_frame, text='Login', compound="top")
        btn_login.grid(row=4, column=0, sticky="NSEW", pady=12, padx=30)

        for child in main_frame.winfo_children():
            main_frame.rowconfigure(child.grid_info()['row'], weight=1, minsize=100)
            main_frame.columnconfigure(child.grid_info()['column'], weight=1, minsize=500)


class NavigationFrame(customtkinter.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        # set grid layout
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=15)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(root, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Navigation",
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Buttons to navigate
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        for child in self.navigation_frame.winfo_children():
            # self.navigation_frame.rowconfigure(child.grid_info()['row'], weight=1)
            self.navigation_frame.columnconfigure(child.grid_info()['column'], weight=1)

        # Appearance changer
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame,
                                                                values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent")

        # create second frame
        self.second_frame = Login(root)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

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

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()