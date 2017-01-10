import datetime
import sys
from PyQt4 import QtGui
from time import sleep as wait


class Reminder(QtGui.QMessageBox):
    def __init__(self):
        super(Reminder, self).__init__()
        QtGui.QMessageBox.information(self, 'TimeCard Reminder',
                                   "<b><font color='#008080'>Please fill your this week\'s Timecard. <br><br></b>"
                                   "<font color='#008080'>Go to <a href='https://www.google.com/'>Timcard Fill Website</a> website...")

    def remind_again(self):
        reply = QtGui.QMessageBox.question(self, 'TimeCard Reminder',
                                           "<b><font color='#8C001A'>Have you filled your this week\'s Timecard?<br><br></b>"
                                           "<font color='#008080'>Go to <a href='https://www.google.com/'>Timcard Fill Website</a> website...", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if not reply == 16384:
            QtGui.QMessageBox.about(self, 'TimeCard Reminder',
                                "<font color='#008080'>You seems little busy now... :)<b><br> No worries...<br></b><font color='#008080'>Will remind you again after <b>30 minutes</b>...")
        return reply

    def thanks(self):
        QtGui.QMessageBox.about(self, 'TimeCard Reminder',
                                "<b><font color='#008080'>Thank you...!!!</b><br><font color='#008080'>Bye for now... Will remind you again on <b>next Friday</b>...")


def main():
    app = QtGui.QApplication(sys.argv)
    while True:
        t = datetime.datetime.today()
        if t.weekday() == 4 and t.hour > 9:
            r = Reminder()
            ret = 0
            while not ret == 16384:
                wait(1800)
                ret = r.remind_again()
            r.thanks()
            wait(20*3600)  # Wait for 20hours
        wait(3600)

if __name__ == '__main__':
    main()
