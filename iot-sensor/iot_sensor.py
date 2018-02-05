from sense_hat import SenseHat
from time import sleep
from random import randrange
from time import time
import requests

sense = SenseHat()

# The URL of the database server (github.com/pohjois-tapiolan-lukio/iot-server)
iot_server_url = "http://iot.olarinlukio.fi:5000"
# The name of the db this script will create and store information in
db_name = "testdemo"

# Maps a value (temperature in celsius) to the amount of lit up pixels (0-6)
def map_to_leds(value, start, end):
    return int(max(0, min(1, (value - start) / (end - start))) * 6)

# Displays a value in a histogram at stat_position
#
# stat_position is 0-2, decides the horizontal position of the visualization (left-to-right)
# range_start and range_end define the stat's desired min and max values
# r, g and b decide the stat visualization's color
def display_stat(stat_position, value, range_start, range_end, r, g, b):
    global sense
    value = map_to_leds(value, range_start, range_end)
    for y in range(7 - value, 7):
        sense.set_pixel(1 + stat_position * 2, y, r, g, b)
        sense.set_pixel(2 + stat_position * 2, y, r, g, b)

# Initialize the database that the data will be stored in
def init_db():
    requests.get("{:s}/database/{:s}/create/time;temperature;pressure;humidity".format(iot_server_url, db_name))

# Send a data point to the database
def send_data(time, temp, pressure, humidity):
    requests.get("{:s}/database/{:s}/insert/{:f};{:f};{:f};{:f}".format(iot_server_url, db_name, time, temp, pressure, humidity))


init_db()
while True:
    # Poll the sensors
    temp = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    # Send the data
    send_data(time(), temp, pressure, humidity)
    # Display the values
    sense.clear()
    display_stat(0, temp, 22, 28, 255, 128, 0)
    display_stat(1, pressure, 1033, 1035, 160, 160, 160)
    display_stat(2, humidity, 17, 28, 0, 128, 255)
    sleep(1)
