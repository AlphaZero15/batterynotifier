from pynotifier import Notification
import psutil
battery = psutil.sensors_battery()
percent = battery.percent
Notification("battery percentage", str(percent) + "%percent remaining", duration=10).send()
