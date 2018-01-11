from sense_hat import SenseHat
from time import sleep
from random import randrange

sense = SenseHat()
sense.clear()
# How many Gs trigger the shaking
shake_threshold = 1.0

def apply_color(rgb):
    pixel_list = []
    for i in range(8 * 8):
        pixel_list.append(rgb)
    sense.set_pixels(pixel_list)

def generate_color():
    return [randrange(50, 255), randrange(50, 255), randrange(50, 255)]

while True:
    accel = sense.get_accelerometer_raw()
    if accel["x"] > shake_threshold or accel["y"] > shake_threshold or accel["z"] - 1 > shake_threshold:
        apply_color(generate_color())
        sleep(3)
        temp = sense.get_temperature()
        pressure = sense.get_pressure()
        sense.show_message("{:.1f} C   {:.1f} hPa".format(temp, pressure))
        sleep(1)
