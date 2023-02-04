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
                               wrap='word', cursor='')

        # Collapse button
        self.collapse_button = ct.CTkButton(self.textbox, text='Collapse all', command=self.collapse_all)
        self.textbox.window_create('0.0', window=self.collapse_button, pady=15)
        self.textbox.insert('end', "\n")

        # Initializes the table of contents
        table_of_contents = []

        self.create_questions()
        counter = 1
        for question in self.questions:
            # Puts text into textbox
            self.textbox.insert("end", question[0], ("heading", f'Q{str(counter)}'))
            self.textbox.insert("end", question[1], ("answer", f'Q{str(counter)}'))
            # Hides the question
            self.textbox.tag_configure(f'Q{str(counter)}', elide=True)

            # Adds the question to table of contents, which means the TOC updates automatically as questions are added
            table_of_contents.insert(0, [question[0] + "\n", f'tocQ{str(counter)}'])

            counter += 1

        new_counter = 0
        # Puts each question from the table of contents into the textbox with a unique tag
        for question in table_of_contents:
            if new_counter < len(table_of_contents):
                self.textbox.insert('0.0', question[0], ("answer", question[1]))
                new_counter += 1
        self.textbox.insert('0.0', "Contents\n", "heading")
        self.textbox.insert('0.0', "\nClick on a question under Contents to expand it.\n", "answer")

        # Sets textbox to be read only
        self.textbox.configure(state='disabled')

        # Scrollbar
        self.scroll_y = ct.CTkScrollbar(self, orientation="vertical", command=self.textbox.yview)
        self.textbox.configure(yscrollcommand=self.scroll_y.set)

        # Gridding
        self.textbox.grid(row=0, column=0, sticky="NEWS", padx=10, pady=10)
        self.scroll_y.grid(row=0, column=1, sticky="NS", pady=10)

        self.tag_binds()
        self.text_formatting()

    # Adds a question into the list of questions
    def add_to_list_of_questions(self, question_heading, question_answer):
        question = [question_heading, question_answer]
        self.questions.append(question)

    # Here, the text is created and appended to self.questions
    def create_questions(self):
        # Don't edit these or the text formatting will be messed up.
        question1_heading = " Q1: How do I add new students to the database?"
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

        question2_heading = " Q2: How do I edit an existing student’s information?"
        question2_answer = """
    Note: To give students points, please see Q7: How do I mark that students have attended an event?/How do I add or remove a student’s points?

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
        question3_heading = " Q3: How do I remove a student from the database?"
        question3_answer = """
    1.  Go to the Students page by clicking on Students on the navigation menu on the left side of the screen. 
    2.  Make sure to navigate to the Edit Students tab by clicking on the Edit button located in the top right corner. It should say “Edit student details:” on your screen. 
    3.  In the list of students, double click the student you wish to remove. On the right, it should say the student’s full name after “Student selected:”.
    4.  Click the red Delete button. 
    5.  Click OK on the confirmation popup. The student should now be removed from the database on the center of the screen. 
"""
        question4_heading = " Q4: How do I add new events to the database?"
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
        question5_heading = " Q5: How do I edit an existing event’s information?"
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
        question6_heading = " Q6: How do I remove an event from the database?"
        question6_answer = """
    1.  Go to the Events page by clicking on Events on the navigation menu on the left side of the screen. 
    2.  Make sure to navigate to the Add Events tab by clicking on the Add tab button located in the top right. 
    3.  In the list of events, click on the event you would like to remove. 
    4.  Click the Delete Event button. 
    5.  Click OK on the confirmation popup. The event should now be removed from the database on the center of the screen. 
"""
        question7_heading = " Q7: How do I mark that students have attended an event?/How do I change a student’s points?"
        question7_answer = """
    1.  Check that the student and event is in the database. If not, add the students and events to the database. (For more information, see Q1: How do I add new students to the database? and Q4: How do I add new events to the database?). 
    2.  Go to the Events page by clicking on Events on the navigation menu on the top of the screen. 
    3.  Make sure to navigate to the Attendance tab by clicking on the Attendance button located in the top right. 
    4.  In the list of events, select the event that the student attended by clicking on it. The event’s name should appear on your screen. 
    5.  In the drop down menu, select the student that attended the event. Alternatively, you can use a scanner to scan physical barcodes into the text field. (For more information, see Q9: How do I use a scanner to add attendees to an event?)
    6.  Click on the Add Student button to save the data. The student’s name and ID should be added to the List of attendees on the left. 
    7.  Repeat steps 5-6 as needed for as each student that attended the event. Each student will receive one point for attending the event.
"""
        question8_heading = " Q8: How do I remove an attendee from an event?/How do I change a student’s points?"
        question8_answer = """
    1.  Go to the Events page by clicking on Events on the navigation menu on the top of the screen. 
    2.  Make sure to navigate to the Attendance tab by clicking on the Attendance button located in the top right. 
    3.  In the list of events, select the event that the student attended by clicking on it. The event’s name should appear on your screen. 
    4.  In the List of attendees, find and select the student who you wish you remove from the event. 
    5.  Click on the red Remove Student button. The student should now be removed from the List of attendees. 
"""

        question9_heading = " Q9: How do I use a scanner to add attendees to an event?"
        question9_answer = """
    1.  Check that the student and event is in the database. If not, add the students and events to the database. (For more information, see Q1: How do I add new students to the database? and Q4: How do I add new events to the database?). 
    2.  Go to the Events page by clicking on Events on the navigation menu on the top of the screen. 
    3.  Make sure to navigate to the Attendance tab by clicking on the Attendance button located in the top right. 
    4.  In the list of events, select the event that the student attended by clicking on it. The event’s name should appear on your screen. 
    5.  Click into the text field where the drop down menu is, then scan the barcode. The student ID should appear in the text field. 
    6.  Click on the Add Student button to save the data. The student’s name and ID should be added to the List of attendees on the left. 
    7.  Repeat steps 5-6 as needed for as each student that attended the event. Each student will receive one point for attending the event.
"""
        question10_heading = " Q10: How do I generate a report at the end of the quarter to find the winners?"
        question10_answer = """
    1.  Go to the Report page by clicking on Report on the navigation menu on the top of the screen. 
    2.  Click on the button that says Click to end quarter. 
    3.  In the popup window, enter a name for the report.
    4.  Click Ok. The report’s results should appear on the screen, along with the winners and the prizes they earned. If you have previously generated reports, you can navigate between the reports by clicking the arrow buttons. 

Note: When a report is created, all of the current events are archived and all student’s points are reset. The archived events can still be viewed under Archived Events in the Events tab. 
"""
        question11_heading = " Q11: How do I add new prizes?"
        question11_answer = """
    1.  Go to the Report page by clicking on Report on the navigation menu on the top of the screen. 
    2.  Click the button that says Add prize.
    3.  In the popup window, enter the name for the prize and click Ok.
    4.  Enter in the number of points required to get the prize and click Ok. The prize should now appear in the list of prizes. 
"""
        question12_heading = " Q12: How do I edit existing prizes?"
        question12_answer = """
    1.  Go to the Report page by clicking on Report on the navigation menu on the top of the screen. 
    2.  Double click on the prize that you would like to edit. The two text fields at the bottom should be automatically filled out with the prize name and points. 
    3.  Change the prize name or points that you would like to edit.
    4.  Click on the Edit prize button to save the changes. The list of prizes should be updated. 
"""
        question13_heading = " Q13: How do I remove existing prizes?"
        question13_answer = """
    1.  Go to the Report page by clicking on Report on the navigation menu on the top of the screen. 
    2.  Click on the prize you want to delete. 
    3.  Click on the Delete prize button. 
    4.  Click OK on the confirmation popup. The prize should now be removed from the list of prizes. 
"""
        self.add_to_list_of_questions(question1_heading, question1_answer)
        self.add_to_list_of_questions(question2_heading, question2_answer)
        self.add_to_list_of_questions(question3_heading, question3_answer)
        self.add_to_list_of_questions(question4_heading, question4_answer)
        self.add_to_list_of_questions(question5_heading, question5_answer)
        self.add_to_list_of_questions(question6_heading, question6_answer)
        self.add_to_list_of_questions(question7_heading, question7_answer)
        self.add_to_list_of_questions(question8_heading, question8_answer)
        self.add_to_list_of_questions(question9_heading, question9_answer)
        self.add_to_list_of_questions(question10_heading, question10_answer)
        self.add_to_list_of_questions(question11_heading, question11_answer)
        self.add_to_list_of_questions(question12_heading, question12_answer)
        self.add_to_list_of_questions(question13_heading, question13_answer)

    def tag_binds(self):
        # When a question in the table of contents is clicked, this shows the text.
        self.textbox.tag_bind('tocQ1', '<Button-1>', lambda x: self.textbox.tag_configure('Q1', elide=False))
        self.textbox.tag_bind('tocQ2', '<Button-1>', lambda x: self.textbox.tag_configure('Q2', elide=False))
        self.textbox.tag_bind('tocQ3', '<Button-1>', lambda x: self.textbox.tag_configure('Q3', elide=False))
        self.textbox.tag_bind('tocQ4', '<Button-1>', lambda x: self.textbox.tag_configure('Q4', elide=False))
        self.textbox.tag_bind('tocQ5', '<Button-1>', lambda x: self.textbox.tag_configure('Q5', elide=False))
        self.textbox.tag_bind('tocQ6', '<Button-1>', lambda x: self.textbox.tag_configure('Q6', elide=False))
        self.textbox.tag_bind('tocQ7', '<Button-1>', lambda x: self.textbox.tag_configure('Q7', elide=False))
        self.textbox.tag_bind('tocQ8', '<Button-1>', lambda x: self.textbox.tag_configure('Q8', elide=False))
        self.textbox.tag_bind('tocQ9', '<Button-1>', lambda x: self.textbox.tag_configure('Q9', elide=False))
        self.textbox.tag_bind('tocQ10', '<Button-1>', lambda x: self.textbox.tag_configure('Q10', elide=False))
        self.textbox.tag_bind('tocQ11', '<Button-1>', lambda x: self.textbox.tag_configure('Q11', elide=False))
        self.textbox.tag_bind('tocQ12', '<Button-1>', lambda x: self.textbox.tag_configure('Q12', elide=False))
        self.textbox.tag_bind('tocQ13', '<Button-1>', lambda x: self.textbox.tag_configure('Q13', elide=False))

        # Makes the table of contents clicky. Some of the scrolling is hardcoded in with line indices
        # self.textbox.tag_bind('tocQ1', '<Button-1>', lambda x: self.textbox.see('Q1.first + 11 lines'))
        # self.textbox.tag_bind('tocQ2', '<Button-1>', lambda x: self.textbox.see('Q2.first + 8 lines'))
        # self.textbox.tag_bind('tocQ3', '<Button-1>', lambda x: self.textbox.see('Q3.first + 8 lines'))
        # self.textbox.tag_bind('tocQ4', '<Button-1>', lambda x: self.textbox.see('Q4.first + 8 lines'))
        # self.textbox.tag_bind('tocQ5', '<Button-1>', lambda x: self.textbox.see('Q5.first + 8 lines'))
        # self.textbox.tag_bind('tocQ6', '<Button-1>', lambda x: self.textbox.see('Q6.first + 8 lines'))
        # self.textbox.tag_bind('tocQ7', '<Button-1>', lambda x: self.textbox.see('Q7.first + 8 lines'))
        # self.textbox.tag_bind('tocQ8', '<Button-1>', lambda x: self.textbox.see('Q8.first + 8 lines'))
        # self.textbox.tag_bind('tocQ9', '<Button-1>', lambda x: self.textbox.see('Q9.first + 8 lines'))
        # self.textbox.tag_bind('tocQ10', '<Button-1>', lambda x: self.textbox.see('Q10.first + 7 lines'))
        # self.textbox.tag_bind('tocQ11', '<Button-1>', lambda x: self.textbox.see('Q11.first + 8 lines'))
        # self.textbox.tag_bind('tocQ12', '<Button-1>', lambda x: self.textbox.see('Q12.first + 8 lines'))
        # self.textbox.tag_bind('tocQ13', '<Button-1>', lambda x: self.textbox.see('Q13.first + 8 lines'))

    # Hides all the questions and answers, not including the table of contents.
    def collapse_all(self):
        self.textbox.tag_configure('Q1', elide=True)
        self.textbox.tag_configure('Q2', elide=True)
        self.textbox.tag_configure('Q3', elide=True)
        self.textbox.tag_configure('Q4', elide=True)
        self.textbox.tag_configure('Q5', elide=True)
        self.textbox.tag_configure('Q6', elide=True)
        self.textbox.tag_configure('Q7', elide=True)
        self.textbox.tag_configure('Q8', elide=True)
        self.textbox.tag_configure('Q9', elide=True)
        self.textbox.tag_configure('Q10', elide=True)
        self.textbox.tag_configure('Q11', elide=True)
        self.textbox.tag_configure('Q12', elide=True)
        self.textbox.tag_configure('Q13', elide=True)

    def text_formatting(self):
        # Yes, these indices are hard coded in. They add formatting on certain words.
        # Bolds the Student ID, Grade Level, First name, Last name, Letter grade in Q1 and Q2.
        # Also bolds the same things for events.
        self.textbox.tag_add('bold', 'Q1.first + 4l + 17c', 'Q1.first + 4l + 27c',
                             'Q1.first + 5l + 17c', 'Q1.first + 5l + 28c',
                             'Q1.first + 6l + 17c', 'Q1.first + 6l + 27c',
                             'Q1.first + 7l + 17c', 'Q1.first + 7l + 26c',
                             'Q1.first + 8l + 17c', 'Q1.first + 8l + 29c',
                             'Q2.first + 7l + 17c', 'Q2.first + 7l + 27c',
                             'Q2.first + 8l + 17c', 'Q2.first + 8l + 28c',
                             'Q2.first + 9l + 17c', 'Q2.first + 9l + 27c',
                             'Q2.first + 10l + 17c', 'Q2.first + 10l + 26c',
                             'Q2.first + 11l + 17c', 'Q2.first + 11l + 29c',
                             'Q4.first + 4l + 17c', 'Q4.first + 4l + 27c',
                             'Q4.first + 5l + 17c', 'Q4.first + 5l + 21c',
                             'Q4.first + 6l + 17c', 'Q4.first + 6l + 19c',
                             'Q4.first + 7l + 17c', 'Q4.first + 7l + 23c',
                             'Q4.first + 8l + 17c', 'Q4.first + 8l + 29c',
                             'Q5.first + 5l + 17c', 'Q5.first + 5l + 27c',
                             'Q5.first + 6l + 17c', 'Q5.first + 6l + 21c',
                             'Q5.first + 7l + 17c', 'Q5.first + 7l + 19c',
                             'Q5.first + 8l + 17c', 'Q5.first + 8l + 23c',
                             'Q5.first + 9l + 17c', 'Q5.first + 9l + 29c')
        # Makes the word 'required' red
        self.textbox.tag_add('red', 'Q1.first + 4l + 28c', 'Q1.first + 4l + 38c',
                             'Q1.first + 5l + 29c', 'Q1.first + 5l + 39c',
                             'Q1.first + 6l + 28c', 'Q1.first + 6l + 38c',
                             'Q1.first + 7l + 27c', 'Q1.first + 7l + 37c',
                             'Q1.first + 8l + 30c', 'Q1.first + 8l + 40c',
                             'Q2.first + 7l + 28c', 'Q2.first + 7l + 38c',
                             'Q2.first + 8l + 29c', 'Q2.first + 8l + 39c',
                             'Q2.first + 9l + 28c', 'Q2.first + 9l + 38c',
                             'Q2.first + 10l + 27c', 'Q2.first + 10l + 37c',
                             'Q2.first + 11l + 30c', 'Q2.first + 11l + 40c',
                             'Q4.first + 4l + 28c', 'Q4.first + 4l + 38c',
                             'Q4.first + 5l + 22c', 'Q4.first + 5l + 32c',
                             'Q4.first + 6l + 20c', 'Q4.first + 6l + 30c',
                             'Q5.first + 5l + 28c', 'Q5.first + 5l + 38c',
                             'Q5.first + 6l + 22c', 'Q5.first + 6l + 32c',
                             'Q5.first + 7l + 20c', 'Q5.first + 7l + 30c')
        # Makes the word 'optional' blue
        self.textbox.tag_add('blue', 'Q4.first + 7l + 24c', 'Q4.first + 7l + 34c',
                             'Q4.first + 8l + 30c', 'Q4.first + 8l + 40c',
                             'Q5.first + 8l + 24c', 'Q5.first + 8l + 34c',
                             'Q5.first + 9l + 30c', 'Q5.first + 9l + 40c')
        # When referring to another question, that question is italicized.
        self.textbox.tag_add('italic', 'Q2.first + 1l + 46c', 'Q2.first + 1l lineend',
                             'Q7.first + 1l + 141c', 'Q7.first + 1l + 187c',
                             'Q7.first + 1l + 192c', 'Q7.first + 1l + 236c',
                             'Q7.first + 5l + 186c', 'Q7.first + 5l + 242c',
                             'Q9.first + 1l + 141c', 'Q9.first + 1l + 187c',
                             'Q9.first + 1l + 192c', 'Q9.first + 1l + 236c')

        # Adds text formatting
        self.textbox.tag_configure('heading', font=('Arial', 24, 'bold underline'), spacing1=36, spacing3=18)
        self.textbox.tag_configure('answer', font=('Arial', 18), spacing2=9, spacing3=9)
        self.textbox.tag_configure('bold', font=('Arial', 18, 'bold'))
        self.textbox.tag_configure('italic', font=('Arial', 18, 'italic'))
        self.textbox.tag_configure('red', foreground='#ff0000')
        self.textbox.tag_configure('blue', foreground='#3366ff')


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
