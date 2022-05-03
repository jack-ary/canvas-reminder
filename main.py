from canvasapi import Canvas
from plyer import notification
from datetime import *
from dateutil import tz
# import sched
# import time

API_URl = "https://canvas.yourSchool.edu"
API_KEY = "YOUR_API_KEY"

canvas = Canvas(API_URl, API_KEY)
user = canvas.get_user(62776)
events = canvas.get_upcoming_events()

# scheduler = sched.scheduler(time.time, time.sleep)


def iso_to_local(iso):
    """
    Converts a complete iso-8601 string to the machines current time zone. Main logic from:

    :param iso: iso-8601 string containing a complete time in UTC
    :return: a string in the format "YYYY-MM-DD 00:00:00-7:00" with the time in the current time zone
    """
    from_zone = tz.gettz('UTC')
    iso = iso[0:10] + " " + iso[11:19]
    utc = datetime.strptime(iso, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    current_zone = utc.astimezone(None)  # None uses the machines time zone here
    return str(current_zone)


def assigns_due_today():
    """
    :return: a string of assignments by title that are due on the current date (due today)
    or all day assignments/events
    """
    due_today = ""
    for e in events:
        if e['all_day']:
            due_date = e['all_day_date']
            if due_date[0:10] == str(date.today()):
                due_today = due_today + e['title'] + "\n"
        else:
            due_date = e['start_at']
            due_date = iso_to_local(due_date)
            if due_date[0:10] == str(date.today()):
                due_today = due_today + e['title'] + "\n"
       

    if due_today == "":
        due_today = "Nothing due the rest of the day :)"
    notification.notify(title='Due today:', message=due_today, app_icon=None, timeout=10)


assigns_due_today()

