from datetime import datetime

def get_oncall_from_google_calendar():
    """
    Simulates reading today's on-call person
    from Google Calendar event title
    """

    fake_calendar = {
        "Monday": "satya",
        "Tuesday": "john",
        "Wednesday": "shanny",
        "Thursday": "satya",
        "Friday": "john",
        "Saturday": "shanny",
        "Sunday": "satya"
    }

    today = datetime.today().strftime("%A")
    return fake_calendar.get(today)