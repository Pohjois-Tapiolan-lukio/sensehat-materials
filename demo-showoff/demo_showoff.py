from sense_hat import SenseHat
from time import sleep
import atexit
import color_shaker
import compass
import environment_sensor

sense = SenseHat()
sense.clear()
current_demo = 0
demo_count = 3

atexit.register(lambda: sense.clear())

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            sense.clear()
            if event.direction == "right" or event.direction == "down":
                current_demo += 1
            elif event.direction == "left" or event.direction == "up":
                current_demo -= 1
            while current_demo >= demo_count and demo_count != 0:
                current_demo -= demo_count
            while current_demo < 0 and demo_count != 0:
                current_demo += demo_count
    if current_demo == 0:
        color_shaker.update(sense)
    elif current_demo == 1:
        compass.update(sense)
    elif current_demo == 2:
        environment_sensor.update(sense)
    sleep(0.1)
