# my_tool.py
# Author: Madison Guss


class AppointmentLookup:
    """A tool that knows available appointment times. It knows nothing about chatting."""

    def __init__(self, schedule):
        """Store the schedule dictionary (day → list of times)."""
        self.schedule = schedule

    def find_day(self, text):
        """Return the first known day mentioned in the text, or None."""
        text_lower = text.lower()
        for day in self.schedule:
            if day in text_lower:
                return day
        return None

    def open_times(self, day):
        """Return the list of open times for a day, or None if the day is unknown."""
        if day in self.schedule:
            return self.schedule[day]
        return None
