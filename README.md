# canvas-reminder
Desktop notifier for canvas assignments and information
# Implementation:
1. Use the command line to install the correct libraries 

`pip install canvas api`
   
`pip install plyer`

`pip install python-dateutil`

2. Obtain your canvas user-id, the five-digit number at the end of your canvas URL
   
`https://canvas.schoolname.edu/about/12345`

3. Obtain your API access key from your canvas profile settings under 'approved integrations'


4. Paste your canvas URL, API access key, and user-id into main.py 

# References: 
https://canvasapi.readthedocs.io/en/stable/getting-started.html

https://python.plainenglish.io/how-to-send-desktop-notifications-with-python-62a738850fbf

https://github.com/mattg1243/whats-due-bot/blob/main/src/main.py

https://stackoverflow.com/questions/68664644/how-can-i-convert-from-utc-time-to-local-time-in-python

https://www.geeksforgeeks.org/sched-module-in-python/