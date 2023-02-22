# Attendance_Tracker_FBLA

The “Attendance Tracker” is a program intended to encourage school spirit by keeping track of student attendance at school events and rewarding the most active students.
This program was made using the python programming language. The code follows the object-oriented programming paradigm and the MVC design pattern. The GUI was created using Tkinter and CustomTkinter while the Matplotlib was used for the graph on the home screen.


The intended user of this program is a teacher or other school staff member. The user can add new students and events into the system as needed. To add a student, the user must enter the student’s ID, grade level, first name, last name, and letter grade. 


To create an event, the user must provide the event’s name, date, ID, nature, and description. Each of these students and events can be edited and deleted as necessary. 


# Documentation
The Attendance Tracker program can do the following:
* Add new students
* Edit and delete existing students
* Add new events
* Edit and delete existing events
* Mark and keep track of student attendance at events
* Use a ID barcode scanner to mark attendance 
* Add new prizes
* Edit and delete existing prizes
* Generate a report to analyze attendance information
* Generate winners and assign prizes to them

Please refer to the FAQ section below for more information. 

## FAQ Table of Contents
* Q1: How do I add new students to the database?
* Q2: How do I edit an existing student’s information?
* Q3: How do I remove a student from the database?
* Q4: How do I add new events to the database?
* Q5: How do I edit an existing event’s information?
* Q6: How do I remove an event from the database?
* Q7: How do I mark that students have attended an event?/How do I change a student’s points?
* Q8: How do I remove an attendee from an event?/How do I change a student’s points?
* Q9: How do I use a scanner to add attendees to an event?
* Q10: How do I generate a report at the end of the quarter to find the winners?
* Q11: How do I add new prizes?
* Q12: How do I edit existing prizes?
* Q13: How do I remove existing prizes?

### Q1: How do I add new students to the database?

1.  Go to the Students page by clicking on Students on the navigation menu on the top of the screen. 
2.  Make sure to navigate to the Add Students tab by clicking on the Add button located in the top right corner. It should say “Add a new student:” on your screen. 
3.  You can enter the student’s information in the corresponding text fields and drop down menus on the right. Filling out all fields is required. 
    -  The Student ID (required) may be any 8 digit number that starts with 5801 and is not already assigned to an existing student. 
    -  The Grade Level (required) should be selected from one of the values on the drop down menu: 9, 10, 11, or 12. 
    -  The First name (required) should be the student’s legal first name and may only contain letters, spaces, and hyphens. 
    -  The Last name (required) should be the student’s legal last name and may only contain letters, spaces, and hyphens. 
    -  The Letter grade (required) should be the student’s current grade and selected from the drop down menu. 
4.  Click the Save button. If there is an issue with data entry, a popup window will appear and describe the error. If so, go back to step 3 and adjust the appropriate fields to address the issue. If the student has been successfully added, the new student should appear in the list of students on the center of the screen.


### Q2: How do I edit an existing student’s information?
 Note: To give students points, please see Q7: How do I mark that students have attended an event?/How do I add or remove a student’s points?
 
 1.  Go to the Students page by clicking on Students on the navigation menu on the top of the screen. 
 2.  Make sure to navigate to the Edit Students tab by clicking on the Edit button located in the top right corner. It should say “Edit student details:” on your screen. 
 3.  In the list of students, double click the student whose information you would like to edit. The The text fields and drop down menus on the right should now be automatically filled with that student’s information. 
 4.  Edit the student’s information by changing the appropriate fields. 
       -  The Student ID (required) may be any 8 digit number that starts with 5801 and is not already assigned to an existing student. 
       -  The Grade Level (required) should be selected from one of the values on the drop down menu: 9, 10, 11, or 12. 
       -  The First name (required) should be the student’s legal first name and may only contain letters, spaces, and hyphens. 
       -  The Last name (required) should be the student’s legal last name and may only contain letters, spaces, and hyphens. 
       -  The Letter grade (required) should be the student’s current grade and selected from the drop down menu. 
 5.  Click the Save button. If there is an issue with data entry, a popup window will appear and describe the error. If so, go back to step 4 and adjust the appropriate fields to address the issue. If the student has been successfully added, the student’s updated information should appear in the list of students on the center of the screen. 



### Q3: How do I remove a student from the database?

   1.  Go to the Students page by clicking on Students on the navigation menu on the top of the screen.
   2.  Make sure to navigate to the Edit Students tab by clicking on the Edit button located in the top right corner. It should say “Edit student details:” on your screen. 
   3.  In the list of students, double click the student you wish to remove. On the right, it should say the student’s full name after “Student selected:”.
   4.  Click the red Delete button. 
   5.  Click OK on the confirmation popup. The student should now be removed from the database on the center of the screen. 

### Q4: How do I add new events to the database?

   1.  Go to the Events page by clicking on Events on the navigation menu on the top of the screen. 
   2.  Make sure to navigate to the Add Events tab by clicking on the Add tab button located in the top right. 
   3.  You can enter the event’s details in the corresponding text fields.
         -  The Event Name (required) should be at least one letter long and may only contain letters and spaces. 
         -  The Date (required) should be in the MM/DD/YYYY format. 
         -  The ID (required) may be any 8 digit number that starts with 9218 and is not already assigned to an existing event. 
         -  The Nature (optional) is the kind of event, such as sport, conference, party, celebration, concert, etc. The Nature may only contain letters and spaces. 
         -  The Description (optional) may include letters, numbers, spaces, and special characters. 
   4.  Click the Save button. If there is an issue with data entry, a popup window will appear and describe the error. If so, go back to step 3 and adjust the appropriate fields to address the issue. If the event has been successfully added, the new event should appear in the list of event on the center of the screen. 


### Q5: How do I edit an existing event’s information? 

   1.  Go to the Events page by clicking on Events on the navigation menu on the top of the screen.
   2.  Make sure to navigate to the Edit Events tab by clicking on the Edit tab button located in the top right. 
   3.  In the list of events, double click the event whose information you would like to edit. The The text fields on the right should now be automatically filled with the event’s information. 
   4.  Edit the event’s information by changing the appropriate fields. 
         -  The Event Name (required) should be at least one letter long and may only contain letters and spaces. 
         -  The Date (required) should be in the MM/DD/YYYY format. 
         -  The ID (required) may be any 8 digit number that starts with 9218 and is not already assigned to an existing event. 
         -  The Nature (optional) is the kind of event, such as sport, conference, party, celebration, concert, etc. The Nature may only contain letters and spaces. 
         -  The Description (optional) may include letters, numbers, spaces, and special characters. 
   4.  Click the Save button. If there is an issue with data entry, a popup window will appear and describe the error. If so, go back to step 3 and adjust the appropriate fields to address the issue. If the event has been successfully added, the new event should appear in the list of event on the center of the screen. 



### Q6: How do I remove an event from the database?

   1.  Go to the Events page by clicking on Events on the navigation menu on the top of the screen.
   2.  Make sure to navigate to the Add Events tab by clicking on the Add tab button located in the top right. 
   3.  In the list of events, click on the event you would like to remove. 
   4.  Click the Delete Event button. 
   5.  Click OK on the confirmation popup. The event should now be removed from the database on the center of the screen. 


### Q7: How do I mark that students have attended an event?/How do I change a student’s points?

   1.  Check that the student and event is in the database. If not, add the students and events to the database. (For more information, see Q1: How do I add new students to the database? and Q4: How do I add new events to the database?). 
   2.  Go to the Events page by clicking on Events on the navigation menu on the top of the screen. 
   3.  Make sure to navigate to the Attendance tab by clicking on the Attendance button located in the top right. 
   4.  In the list of events, select the event that the student attended by clicking on it. The event’s name should appear on your screen. 
   5.  In the drop down menu, select the student that attended the event. Alternatively, you can use a scanner to scan physical barcodes into the text field. (For more information, see Q9: How do I use a scanner to add attendees to an event?)
   6.  Click on the Add Student button to save the data. The student’s name and ID should be added to the List of attendees on the left. 
   7.  Repeat steps 5-6 as needed for as each student that attended the event. Each student will receive one point for attending the event.



### Q8: How do I remove an attendee from an event?/How do I change a student’s points?

   1.  Go to the Events page by clicking on Events on the navigation menu on the top of the screen.
   2.  Make sure to navigate to the Attendance tab by clicking on the Attendance button located in the top right. 
   3.  In the list of events, select the event that the student attended by clicking on it. The event’s name should appear on your screen. 
   4.  In the List of attendees, find and select the student who you wish you remove from the event. 
   5.  Click on the red Remove Student button. The student should now be removed from the List of attendees. 


### Q9: How do I use a scanner to add attendees to an event?

 1.  Check that the student and event is in the database. If not, add the students and events to the database. (For more information, see Q1: How do I add new students to the database? and Q4: How do I add new events to the database?). 
 2.  Go to the Events page by clicking on Events on the navigation menu on the top of the screen. 
 3.  Make sure to navigate to the Attendance tab by clicking on the Attendance button located in the top right. 
 4.  In the list of events, select the event that the student attended by clicking on it. The event’s name should appear on your screen. 
 5.  Click into the text field where the drop down menu is, then scan the barcode. The student ID should appear in the text field. 
 6.  Click on the Add Student button to save the data. The student’s name and ID should be added to the List of attendees on the left. 
 7.  Repeat steps 5-6 as needed for as each student that attended the event. Each student will receive one point for attending the event.



### Q10: How do I generate a report at the end of the quarter to find the winners?

   1.  Go to the Report page by clicking on Report on the navigation menu on the top of the screen. 
   2.  Click on the button that says Click to end quarter. 
   3.  In the popup window, enter a name for the report.
   4.  Click Ok. The report’s results should appear on the screen, along with the winners and the prizes they earned. If you have previously generated reports, you can navigate between the reports by clicking the arrow buttons. 



### Q11: How do I add new prizes?

   1.  Go to the Report page by clicking on Report on the navigation menu on the top of the screen. 
   2.  Click the button that says Add prize.
   3.  In the popup window, enter the name for the prize and click Ok.
   4.  Enter in the number of points required to get the prize and click Ok. The prize should now appear in the list of prizes. 


### Q12: How do I edit existing prizes?

   1.  Go to the Report page by clicking on Report on the navigation menu on the top of the screen. 
   2.  Double click on the prize that you would like to edit. The two text fields at the bottom should be automatically filled out with the prize name and points. 
   3.  Change the prize name or points that you would like to edit.
   4.  Click on the Edit prize button to save the changes. The list of prizes should be updated. 


### Q13: How do I remove existing prizes?

   1.  Go to the Report page by clicking on Report on the navigation menu on the top of the screen. 
   2.  Click on the prize you want to delete. 
   3.  Click on the Delete prize button. 
   4.  Click OK on the confirmation popup. The prize should now be removed from the list of prizes. 

