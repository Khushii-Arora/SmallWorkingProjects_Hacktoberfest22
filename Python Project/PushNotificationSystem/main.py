# this is made using plyer package to send notification
# the schudeling is done with schudeler package

import schedule
import time
from plyer import notification


def my_notification():
    title = "Notification"
    message = "Dear Mrigesh!! Its been days you had a glass of water ... Please drink water and stay healthy"

    notification.notify(title=title,
                        message=message,
                        app_icon=None,
                        timeout=10,
                        toast="Warning!! Get hydrated")


schedule.every(120).minutes.do(my_notification)
while True:
    schedule.run_pending()
    time.sleep(1)
