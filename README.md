"# Timecard-Reminder" 

Hello,

How many times you forgot to fill your timecard and got reminder mail from your manager? Most of the times... at least it happens with me  always . 
I know it happens with all of us one or the other time.

So here is the permanent solution for this. This app will remind you with popup notifications to fill your timecard on every Friday. 

How to install?

1.	Download and save the TimecardReminder app executable(NuanceTimecardReminder.exe)

2.	Copy this exe file to your windows Startup folder:

Go to Start Menu -> All Programs -> Startup or directly open C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup  in windows explorer.

3.	Restart your windows machine once.

4.	That’s it. There is no 4th step .

How it works?

1.	The app will be running in background continuously.

2.	On every Friday from 9:00AM, it will show popup notification as shown below.

	![alt tag](https://github.com/sunilthorat09/Timecard-Reminder/tree/master/screenshots/popup1.PNG)
	
3.	The timecard fill website hyperlink is provided on popup itself which will be opened in browser directly. [Current I have kept Google website link, You need to chnage it to applicable website]

4.	After that it will show another popup to ask if timecard is filled or not after every 30minutes in case if you select ‘NO’ as response.

	![alt tag](https://github.com/sunilthorat09/Timecard-Reminder/tree/master/screenshots/popup2.PNG?raw=true )
	
5.	Reminder popup will be shown till you select ‘YES’ response.

6.	Again same popup notifications will be shown on next Friday.

So now I hope with this app you will never forget to fill your timecard AGAIN.


Note:
After modification in the code, create the new executable with below command:

	pyinstaller.exe --onefile --windowed --icon=app.ico timecard_reminder.py

More info @ https://mborgerson.com/creating-an-executable-from-a-python-script 




