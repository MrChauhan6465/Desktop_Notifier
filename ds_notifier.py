from email import message
import imp
from turtle import title
from plyer import notification 
import time 
if __name__ =='__main__':
    while True :
        notification.notify(
            title = ' Rest kar bhai ',
            message = " It is important to take breaks and rest throughout the day, especially if you are feeling tired or overwhelmed. Taking a few minutes to yourself can help you reenergize and refocus so that you can be more productive.",

            app_icon = 'F:/Python-projects/PYTHONProjects/desktop_notifier/comfort-zone.ico',
            timeout = 10
        )
        time.sleep(1200)


