from canvasapi import Canvas
from plyer import notification
from datetime import *
from dateutil import tz
# import plyer

API_URl = "https://canvas.calpoly.edu"
API_KEY = "15279~egR5cLEo59vojkI9m7U2DvDjFRATI9MG0vnjm6njEE8IxDwGAOTiwUDxNudoVyoM"

canvas = Canvas(API_URl, API_KEY)
user = canvas.get_user(62776)
events = canvas.get_upcoming_events()

due_today = ""


def iso_to_local(iso):
    """
    Converts a complete iso-8601 string to the machines current time zone. Main logic from:

    :param iso: iso-8601 string containing a complete time in UTC
    :return: a string in the format "YYYY-MM-DD 00:00:00-7:00"
    """

    from_zone = tz.gettz('UTC')
    iso = iso[0:10] + " " + iso[11:19]
    utc = datetime.strptime(iso, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    current_zone = utc.astimezone(None)  # None uses the machines time zone here
    return str(current_zone)


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


notification.notify(title='Due today:', message=due_today, app_icon=None, timeout=10)




#https://plyer.readthedocs.io/en/latest/#
#print(events[1]['assignment']['due_at'])


# course = canvas.get_course(78430) # Course Code
# assignments = course.get_assignments()
#
# assignments_response: list = []
# for a in assignments:
#     print(a)
#     assignments_response.append(a)
#     print(a.due_at)




# today = date.today()
# nextWeek = today + timedelta(days=7)
#
# format_str = "%a %b %d"
# response_msg = "What's due in the next 7 days:"
# for a in assignments_response:
#     if date.fromisoformat(a.due_at.split("T")[0]) <= nextWeek:
#         due_date = date.fromisoformat(a.due_at.split("T")[0]).strftime(format_str)
#         response_msg += f"\n{a.name} due {due_date}"
#         print(response_msg)


# for assignment in assignments:
#     print(assignment)


# assignments = course.get_assignments()
# for assignment in assignments:
#     print(assignment)

# courses = canvas.get_courses(enrollment_state='active')
# for course in courses:
#     print(course)

