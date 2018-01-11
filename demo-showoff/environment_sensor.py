from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def map_to_leds(value, start, end):
    return int(max(0, min(1, (value - start) / (end - start))) * 6)

# stat_position is 0-2, decides the horizontal position of the visualization (left-to-right)
# range_start and range_end define the stat's desired min and max values
# r, g and b decide the stat visualization's color
def display_stat(sense, stat_position, value, range_start, range_end, r, g, b):
    value = map_to_leds(value, range_start, range_end)
    for y in range(7 - value, 7):
        sense.set_pixel(1 + stat_position * 2, y, r, g, b)
        sense.set_pixel(2 + stat_position * 2, y, r, g, b)

def update(sense):
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    sense.clear()
    display_stat(sense, 0, temp, 22, 28, 255, 128, 0)
    display_stat(sense, 1, pressure, 1033, 1035, 160, 160, 160)
    display_stat(sense, 2, humidity, 17, 28, 0, 128, 255)
    sleep(0.1)
