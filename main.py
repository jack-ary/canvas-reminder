from canvasapi import Canvas
from plyer import notification
import time

# while True:
notification.notify(title='Canvas Reminder', message='message', app_icon=None, timeout=10)
# time.sleep(30)

API_URl = "https://canvas.calpoly.edu"
API_KEY = "15279~16MobaoYyHNBzFrol9P2cIGNV8Md98g7kI43hVbWvGHUPAaGbKkIxW30bPSL9XMk"

canvas = Canvas(API_URl, API_KEY)
user = canvas.get_user()

course = canvas.get_course(71875)

assignments = course.get_assignments()
for assignment in assignments:
    print(assignment)

courses = canvas.get_courses(enrollment_state='active')
for course in courses:
    print(course)

# Getting user logins:
# logins = user.get_user_logins()
# for login in logins:
#     print(login)

# users = course.get_users()
# for user in users:
#     print(user)
