import pickle


class Event:
    def __init__(self, name: str, date: str, event_description: str, is_sport: bool):
        self.name = name
        self.date = date
        self.event_description = event_description
        self.is_sport = is_sport
        self.attendees = []

    def add_attendee(self, attendee):
        self.attendees.append(attendee)

    def delete_attendee(self, remove_attendee):
        self.attendees = [attendee for attendee in self.attendees if attendee != remove_attendee]


class MetaEvents:
    def __init__(self):
        self.events = []

    def add_event(self, name, date, nature, event_description):
        self.events.append(Event(name, date, nature, event_description))

    def delete_event(self, remove_event):
        self.events = [event for event in self.events if event != remove_event]

    def get_event(self, name):
        for event in self.events:
            if name == event.name:
                return event

    def get_sport_events(self):
        sport_events = [event for event in self.events if event.is_sport]
        return sport_events

    def get_non_sport_events(self):
        non_sport_events = [event for event in self.events if not event.is_sport]
        return non_sport_events

    def load_data(self, file_name='events'):
        with open(f'project_data/events/{file_name}.pkl', 'rb') as data_input:
            self.events = pickle.load(data_input)

    def save_data(self, file_name='events'):
        with open(f'project_data/events/{file_name}.pkl', 'wb') as data_output:
            pickle.dump(self.events, data_output, pickle.HIGHEST_PROTOCOL)
