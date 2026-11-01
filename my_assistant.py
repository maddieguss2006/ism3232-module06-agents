# my_assistant.py
# Author: Madison Guss

HANDOFF_WORDS = ["book", "schedule", "reserve", "cancel"]


class AppointmentAssistant:
    """A mock appointment assistant for a tax office."""

    def __init__(self, name, instructions, appointment_tool):
        self.name = name
        self.instructions = instructions
        self.appointment_tool = appointment_tool
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't change the schedule. I'm passing you to the front desk."
        if "time" in text or "open" in text or "available" in text:
            return self.times_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. Ask me which times are open on a day."
        return "I'm not sure how to help with that. I can list open times."

    def needs_human(self, text):
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def times_reply(self, user_message):
        day = self.appointment_tool.find_day(user_message)
        if day is None:
            return "Which day? I can check Monday, Wednesday, or Friday."
        times = self.appointment_tool.open_times(day)
        times_str = " and ".join(times)
        return f"Open times on {day}: {times_str}."
