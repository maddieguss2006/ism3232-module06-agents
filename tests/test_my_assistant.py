from my_assistant import AppointmentAssistant
from my_tool import AppointmentLookup


def make_bot():
    schedule = {
        "monday": ["9:00 am", "2:30 pm"],
        "wednesday": ["10:00 am"],
    }
    return AppointmentAssistant(
        "Robin",
        "Be helpful.",
        AppointmentLookup(schedule),
    )


def test_finds_known_day():
    tool = AppointmentLookup({"monday": ["9:00 am"]})
    assert tool.find_day("What times are open on Monday?") == "monday"


def test_unknown_day_returns_none():
    tool = AppointmentLookup({"monday": ["9:00 am"]})
    assert tool.find_day("What about Tuesday?") is None


def test_respond_records_history():
    bot = make_bot()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"


def test_times_question_uses_tool():
    bot = make_bot()
    reply = bot.respond("What times are open on Monday?")
    assert "9:00 am" in reply
    assert "2:30 pm" in reply


def test_unknown_day_asks_for_day():
    bot = make_bot()
    assert "Which day" in bot.respond("What is available?")


def test_booking_goes_to_human():
    bot = make_bot()
    assert "front desk" in bot.respond("Please book me for Monday at 9")
