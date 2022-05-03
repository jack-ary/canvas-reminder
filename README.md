# canvas-reminder
Desktop notifier for canvas assignments and information. This program will send a desktop notification telling you what 
assignments are due the day that the program is run. I have my program scheduled to run every day in the morning when I know I will be on my computer. 
See step 5 for scheduling the program to run as a task. 
Note: if an assignment is due before the time that you run the program, it will not be a part of the notification, evening though that assignment 
was still due 'today,' because its due date has already passed. The program does however account for assignments that 
are marked as 'all_day', and they will appear on the desktop notification the day that they are due. The command prompt will automatically open as part of running the program as a task, but you don't have to use it, 
and it will automatically close when the task has been executed. 


# Implementation:
1. Install the correct libraries with the command line:

`pip install canvas api`
   
`pip install plyer`

`pip install python-dateutil`

2. Obtain your canvas user-id, the five-digit number at the end of your canvas URL
   
`https://canvas.schoolname.edu/about/12345`

3. Obtain your API access key from your canvas profile settings under 'approved integrations'


4. Paste your canvas URL, API access key, and user-id into main.py 


5. To schedule when your Windows computer will run the program, you must put it in a task (you must use task scheduler, not task manager). 
Follow [these](http://theautomatic.net/2017/10/03/running-python-task-scheduler/#:~:text=Once%20you%20know%20your%20Python%20script%20works%20from,click%20on%20%E2%80%9CAction%E2%80%9D%2C%20and%20then%20press%20%E2%80%9CCreate%20Task.%E2%80%9D) steps.


# References: 
https://canvasapi.readthedocs.io/en/stable/getting-started.html

https://python.plainenglish.io/how-to-send-desktop-notifications-with-python-62a738850fbf

https://github.com/mattg1243/whats-due-bot/blob/main/src/main.py

https://stackoverflow.com/questions/68664644/how-can-i-convert-from-utc-time-to-local-time-in-python

https://www.geeksforgeeks.org/sched-module-in-python/