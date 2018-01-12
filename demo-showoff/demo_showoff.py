from sense_hat import SenseHat
from time import sleep, time
import atexit
import color_shaker
import compass
import environment_sensor

sense = SenseHat()
sense.clear()
current_demo = 0
demo_count = 3
quit_press_time = -1
running = True

atexit.register(lambda: sense.clear())

while running:
    for event in sense.stick.get_events():
        if current_demo == 2 and environment_sensor.process_input(sense, event):
            continue
        if event.action == "pressed":
            sense.clear()
            if event.direction == "right" or event.direction == "down":
                current_demo += 1
            elif event.direction == "left" or event.direction == "up":
                current_demo -= 1
            elif event.direction == "middle":
                if quit_press_time == -1:
                    quit_press_time = time()
            while current_demo >= demo_count and demo_count != 0:
                current_demo -= demo_count
            while current_demo < 0 and demo_count != 0:
                current_demo += demo_count
        elif event.action == "held":
            if time() - quit_press_time > 4:
                running = False
        elif event.action == "released":
            quit_press_time = -1
    if current_demo == 0:
        color_shaker.update(sense)
    elif current_demo == 1:
        compass.update(sense)
    elif current_demo == 2:
        environment_sensor.update(sense)
    sleep(0.1)
