import customtkinter as ct
import tkinter as tk


class HelpMenu(ct.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.questions = []

        # Initializes textbox
        self.textbox = tk.Text(self, font=('Arial', 20), foreground="#d6d6d6", background="#333333", border=0,
                               wrap='word')

        # Puts text into textbox
        self.create_questions()
        for question in self.questions:
            self.textbox.insert("end", question[0], "heading")
            self.textbox.insert("end", question[1], "answer")

        # Adds styling with fonts
        self.heading_font = ("Arial", 24, "bold")
        self.answer_font = ("Arial", 18)
        self.textbox.tag_configure("heading", font=self.heading_font, spacing1=36, spacing3=18)
        self.textbox.tag_config("answer", font=self.answer_font, spacing2=9, spacing3=9)

        # Sets textbox to be read only
        self.textbox.configure(state='disabled')

        # Scrollbar
        self.scroll_y = ct.CTkScrollbar(self, orientation="vertical", command=self.textbox.yview)
        self.textbox.configure(yscrollcommand=self.scroll_y.set)

        # Gridding
        self.textbox.grid(row=0, column=0, sticky="NEWS", padx=10, pady=10)
        self.scroll_y.grid(row=0, column=1, sticky="NS", pady=10)

    # Adds a question into the list of questions
    def add_to_list_of_questions(self, question_heading, question_answer):
        question = [question_heading, question_answer]
        self.questions.append(question)

    # Here, the text is created and appended to self.questions
    def create_questions(self):
        question1_heading = " How do I add new students to the database?"
        question1_answer = """
    1.  Go to the Students page by clicking on Students on the navigation menu on the left side of the screen. 
    2.  Make sure to navigate to the Add Students tab by clicking on the Add button located in the top right corner. It should say “Add a new student:” on your screen. 
    3.  You can enter the student’s information in the corresponding text fields and drop down menus on the right. Filling out all fields is required. 
          -  The Student ID (required) may be any 8 digit number that starts with 5801 and is not already assigned to an existing student. 
          -  The Grade Level (required) should be selected from one of the values on the drop down menu: 9, 10, 11, or 12. 
          -  The First name (required) should be the student’s legal first name and may only contain letters, spaces, and hyphens. 
          -  The Last name (required) should be the student’s legal last name and may only contain letters, spaces, and hyphens. 
          -  The Letter grade (required) should be the student’s current grade and selected from the drop down menu. 
    4.  Click the Save button. If there is an issue with data entry, a popup window will appear and describe the error. If so, go back to step 3 and adjust the appropriate fields to address the issue. If the student has been successfully added, the new student should appear in the list of students on the center of the screen.
"""

        question2_heading = " How do I edit an existing student’s information?"
        question2_answer = """
    Note: To give students points, please see How do I mark that students have attended an event?/How do I add or remove a student’s points?

    1.  Go to the Students page by clicking on Students on the navigation menu on the left side of the screen. 
    2.  Make sure to navigate to the Edit Students tab by clicking on the Edit button located in the top right corner. It should say “Edit student details:” on your screen. 
    3.  In the list of students, double click the student whose information you would like to edit. The The text fields and drop down menus on the right should now be automatically filled with that student’s information. 
    4.  Edit the student’s information by changing the appropriate fields. 
          -  The Student ID (required) may be any 8 digit number that starts with 5801 and is not already assigned to an existing student. 
          -  The Grade Level (required) should be selected from one of the values on the drop down menu: 9, 10, 11, or 12. 
          -  The First name (required) should be the student’s legal first name and may only contain letters, spaces, and hyphens. 
          -  The Last name (required) should be the student’s legal last name and may only contain letters, spaces, and hyphens. 
          -  The Letter grade (required) should be the student’s current grade and selected from the drop down menu. 
    5.  Click the Save button. If there is an issue with data entry, a popup window will appear and describe the error. If so, go back to step 4 and adjust the appropriate fields to address the issue. If the student has been successfully added, the student’s updated information should appear in the list of students on the center of the screen. 
"""
        question3_heading = "How do I remove a student from the database?"
        question3_answer = """
    1.  Go to the Students page by clicking on Students on the navigation menu on the left side of the screen. 
    2.  Make sure to navigate to the Edit Students tab by clicking on the Edit button located in the top right corner. It should say “Edit student details:” on your screen. 
    3.  In the list of students, double click the student you wish to remove. On the right, it should say the student’s full name after “Student selected:”.
    4.  Click the red Delete button. 
    5.  Click OK on the confirmation popup. The student should now be removed from the database on the center of the screen. 
"""
        question4_heading = " How do I add new events to the database?"
        question4_answer = """
    1.  Go to the Events page by clicking on Events on the navigation menu on the left side of the screen. 
    2.  Make sure to navigate to the Add Events tab by clicking on the Add tab button located in the top right. 
    3.  You can enter the event’s details in the corresponding text fields.
          -  The Event Name (required) should be at least one letter long and may only contain letters and spaces. 
          -  The Date (required) should be in the MM/DD/YYYY format. 
          -  The ID (required) may be any 8 digit number that starts with 9218 and is not already assigned to an existing event. 
          -  The Nature (optional) is the kind of event, such as sport, conference, party, celebration, concert, etc. The Nature may only contain letters and spaces. 
          -  The Description (optional) may include letters, numbers, spaces, and special characters. 
    4.  Click the Save button. If there is an issue with data entry, a popup window will appear and describe the error. If so, go back to step 3 and adjust the appropriate fields to address the issue. If the event has been successfully added, the new event should appear in the list of event on the center of the screen. 
"""
        question5_heading = " How do I edit an existing event’s information?"
        question5_answer = """
    1.  Go to the Events page by clicking on Events on the navigation menu on the left side of the screen. 
    2.  Make sure to navigate to the Edit Events tab by clicking on the Edit tab button located in the top right. 
    3.  In the list of events, double click the event whose information you would like to edit. The The text fields on the right should now be automatically filled with the event’s information. 
    4.  Edit the event’s information by changing the appropriate fields. 
          -  The Event Name (required) should be at least one letter long and may only contain letters and spaces. 
          -  The Date (required) should be in the MM/DD/YYYY format. 
          -  The ID (required) may be any 8 digit number that starts with 9218 and is not already assigned to an existing event. 
          -  The Nature (optional) is the kind of event, such as sport, conference, party, celebration, concert, etc. The Nature may only contain letters and spaces. 
          -  The Description (optional) may include letters, numbers, spaces, and special characters. 
    4.  Click the Save button. If there is an issue with data entry, a popup window will appear and describe the error. If so, go back to step 3 and adjust the appropriate fields to address the issue. If the event has been successfully added, the new event should appear in the list of event on the center of the screen. 
"""
        question6_heading = " How do I remove an event from the database?"
        question6_answer = """
    1.  Go to the Events page by clicking on Events on the navigation menu on the left side of the screen. 
    2.  Make sure to navigate to the Add Events tab by clicking on the Add tab button located in the top right. 
    3.  In the list of events, click on the event you would like to remove. 
    4.  Click the Delete Event button. 
    5.  Click OK on the confirmation popup. The event should now be removed from the database on the center of the screen. 
"""

        self.add_to_list_of_questions(question1_heading, question1_answer)
        self.add_to_list_of_questions(question2_heading, question2_answer)
        self.add_to_list_of_questions(question3_heading, question3_answer)
        self.add_to_list_of_questions(question4_heading, question4_answer)
        self.add_to_list_of_questions(question5_heading, question5_answer)
        self.add_to_list_of_questions(question6_heading, question6_answer)


if __name__ == "__main__":
    # Initializes the window
    window = ct.CTk()
    window.geometry()
    window.title("Attendance Tracker")
    ct.set_appearance_mode("dark")
    ct.set_default_color_theme("dark-blue")

    HelpMenu(window).grid(row=0, column=0)

    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)

    window.mainloop()
