from plyer import notification
import time
while True:
    notification.notify(title='TAKE A BREAK',
                    message="look away at distance of more than 20m for more than 20 seconds",
                    app_icon="eyes.ico",timeout=3)
    time.sleep(3)
    #time.sleep(30*60)
    notification.notify(title='DRINK WATER',
                        message="Drink water to avoid disease",
                        app_icon="glass.ico", timeout=2)
    time.sleep(10)

    notification.notify(title='DAILY EXCERCISE',
                        message="Excercise maintain our fitness and good for health",
                        app_icon="excercise.ico", timeout=2)
    time.sleep(30)


