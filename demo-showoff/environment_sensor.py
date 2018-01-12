from sense_hat import SenseHat
from time import sleep

temperature_variation = 3
pressure_variation = 1
humidity_variation = 5
base_temperature = 25
base_pressure = 1045
base_humidity = 22

def init(sense):
    global base_temperature
    global base_pressure
    global base_humidity
    base_temperature = sense.get_temperature()
    base_pressure = sense.get_pressure()
    base_humidity = sense.get_humidity()

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

def process_input(sense, event):
    if event.action == "pressed" and event.direction == "middle":
        init(sense)
        return True
    return False

def update(sense):
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    sense.clear()
    display_stat(sense, 0, temp, base_temperature - temperature_variation, base_temperature + temperature_variation, 255, 128, 0)
    display_stat(sense, 1, pressure, base_pressure - pressure_variation, base_pressure + pressure_variation, 160, 160, 160)
    display_stat(sense, 2, humidity, base_humidity - humidity_variation, base_humidity + humidity_variation, 0, 128, 255)
    sleep(0.1)
