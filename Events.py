import pickle
import datetime


class Event:
    def __init__(self, event_id: int, name: str, date: str, nature: str, event_description: str):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.event_description = event_description
        self.nature = nature
        self.attendees = []

        self.is_archived = False

    # Using weakreferences to store attendees so that they are deleted when they are deleted from studentmanager list
    # one can call the weakrefernce to access the object by adding a () at the end of the weakreference
    def add_attendee(self, attendee):
        existing_student_ids = [student.student_id for student in self.attendees]
        if attendee.student_id not in existing_student_ids:
            self.attendees.append(attendee)
            attendee.add_points(1)

    def delete_attendee(self, remove_attendee):
        for attendee in self.attendees:
            if attendee.student_id == remove_attendee.student_id:
                self.attendees.remove(attendee)
        remove_attendee.points -= 1 if remove_attendee.points > 0 else 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Event({self.event_id}, {self.name}, {self.date}, nature: {self.nature})"


class EventManager:
    def __init__(self):
        self.events = []
        self.load_data()

    def add_event(self, event_id, name, date, nature, event_description):
        ids = [event.event_id for event in self.events]
        invalid_ids = ['']
        if event_id in ids:
            raise Exception("ID already exists")
        elif event_id in invalid_ids:
            raise Exception('Invalid ID.')
        else:
            self.events.append(Event(event_id, name, date, nature, event_description))

    def delete_event(self, remove_event_id):
        event = self.get_event(remove_event_id)
        self.events.remove(event)

    def get_event(self, id):
        for event in self.events:
            # Enforce ints when doing validation
            if id == str(event.event_id):
                return event

    def get_sport_events(self):
        sport_events = [event for event in self.events if event.nature == 'Sport']
        return sport_events

    def get_non_sport_events(self):
        non_sport_events = [event for event in self.events if not event.nature == 'Sport']
        return non_sport_events

    def load_data(self, file_name='events'):
        with open(f'project_data/events/{file_name}.pkl', 'rb') as data_input:
            self.events = pickle.load(data_input)

    def save_data(self, file_name='events'):
        with open(f'project_data/events/{file_name}.pkl', 'wb') as data_output:
            pickle.dump(self.events, data_output, pickle.HIGHEST_PROTOCOL)

    # Validation Methods
    def validate_id(self, id, event=None):
        if id == "92180000 to 92189999":
            return "\tThe Event ID must be filled out."
        try:
            id = int(id)
        except ValueError:
            return "\tThe Event ID may only include whole numbers."


        ids = [event.event_id for event in self.events]
        if not 92180000 <= id <= 92189999:
            return "\tThe Event ID must be an 8 digit number starting with 9218."
        elif event:
            other_events_id = [e.event_id for e in self.events if e != event]
            if id in other_events_id:
                return "\tThis Event ID is already assigned to another event."
        elif id in ids:
            return '\tThis Event ID is already assigned to another event.'
        return True

    def validate_event_name(self, name):
        if name == "Event Name":
            return "\tThe Event name must be filled out."

        if not name.replace(' ', '').isalpha():
            return '\tThe Event name may only include letters and spaces.'

        return True

    def validate_date(self, date):
        if date == 'In MM/DD/YYYY format':
            return '\tDate must be filled out.'
        try:
            datetime.datetime.strptime(date, '%m/%d/%Y')
        except ValueError:
            return '\tThe Date must be in the MM/DD/YYYY format.'
        month, day, year = date.split('/')
        if len(month) != 2 or len(day) != 2:
            return '\tThe Date must be in the MM/DD/YYYY format.'
        return True

    def validate_nature(self, nature):
        if not nature.replace(' ', '').isalpha():
            return '\tThe Nature may only include letters and spaces.'
        return True


event_manager = EventManager()
