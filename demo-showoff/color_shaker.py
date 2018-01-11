from sense_hat import SenseHat
from time import sleep
from random import randrange

A = (0, 0, 0)
B = (100, 100, 100)
ICON = [
    A, A, A, A, A, A, A, A,
    B, A, A, A, A, A, A, B,
    B, A, A, A, A, A, A, B,
    B, A, B, A, A, B, A, B,
    B, A, B, A, A, B, A, B,
    B, A, A, A, A, A, A, B,
    B, A, A, A, A, A, A, B,
    A, A, A, A, A, A, A, A
]

# How many Gs trigger the shaking
shake_threshold = 2.0

def generate_color():
    return [randrange(50, 255), randrange(50, 255), randrange(50, 255)]

def update(sense):
    sense.set_pixels(ICON)
    accel = sense.get_accelerometer_raw()
    if accel["x"] > shake_threshold or accel["y"] > shake_threshold or accel["z"] - 1 > shake_threshold:
        sense.clear(generate_color())
        sleep(3)
        temp = sense.get_temperature()
        pressure = sense.get_pressure()
        sense.show_message("{:.1f} C   {:.1f} hPa".format(temp, pressure))
        sleep(1)
