from canvasapi import Canvas
from plyer import notification
import time

# while True:
notification.notify(title='Canvas Reminder', message='message', app_icon=None, timeout=10)
# time.sleep(30)

API_URl = "Canvas_URL"
API_KEY = "Access_Token"

canvas = Canvas(API_URl, API_KEY)
user = canvas.get_user()

course = canvas.get_course(12345) # Course Code

assignments = course.get_assignments()
for assignment in assignments:
    print(assignment)

courses = canvas.get_courses(enrollment_state='active')
for course in courses:
    print(course)

