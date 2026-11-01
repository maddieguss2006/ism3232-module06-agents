# my_main.py
# Author: Madison Guss

from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup

SCHEDULE = {
    "monday": ["9:00 am", "2:30 pm"],
    "wednesday": ["10:00 am", "1:00 pm", "4:00 pm"],
    "friday": ["9:30 am", "11:00 am"],
}

tool = AppointmentLookup(SCHEDULE)
bot = AppointmentAssistant(
    "Robin",
    "You are a helpful appointment assistant for a tax office.",
    tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
