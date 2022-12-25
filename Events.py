import pickle


class Event:
    def __init__(self, event_id: int, name: str, date: str, nature: str, event_description: str):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.event_description = event_description
        self.nature = nature
        self.attendees = []

    def add_attendee(self, attendee):
        self.attendees.append(attendee)
        attendee.add_points(1)

    def delete_attendee(self, remove_attendee):
        self.attendees = [attendee for attendee in self.attendees if attendee != remove_attendee]
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
        match = None
        for event in self.events:
            # Enforce ints when doing validation
            if id == str(event.event_id):
                match = event

        if match:
            return match
        else:
            raise Exception('Event not found.')

    def get_sport_events(self):
        sport_events = [event for event in self.events if event.nature == 'Sport']
        return sport_events

    def get_non_sport_events(self):
        non_sport_events = [event for event in self.events if not event.nature != 'Sport']
        return non_sport_events

    def load_data(self, file_name='events'):
        with open(f'project_data/events/{file_name}.pkl', 'rb') as data_input:
            self.events = pickle.load(data_input)

    def save_data(self, file_name='events'):
        with open(f'project_data/events/{file_name}.pkl', 'wb') as data_output:
            pickle.dump(self.events, data_output, pickle.HIGHEST_PROTOCOL)

event_manager = EventManager()