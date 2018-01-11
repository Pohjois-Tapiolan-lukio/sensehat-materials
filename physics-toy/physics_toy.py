from sense_hat import SenseHat
from math import radians, sin, cos
from time import sleep
from random import random

sense = SenseHat()

A = (0, 0, 0)
B = (150, 150, 150)
STABLE = [
    A, A, A, A, A, A, A, A,
    A, A, A, A, A, A, A, A,
    A, A, A, A, A, A, A, A,
    A, A, B, B, B, B, A, A,
    A, A, B, B, B, B, A, A,
    A, A, A, A, A, A, A, A,
    A, A, A, A, A, A, A, A,
    A, A, A, A, A, A, A, A,
]

G = 0.1
zero_rotation = (0, 0, 0)
points = []

def sign(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0

def init(sense):
    global zero_rotation
    global points
    sense.set_pixels(STABLE)
    sleep(1)
    zero_rotation = sense.get_gyroscope()
    points = []
    for i in range(5):
        # [x, y, x_velocity, y_velocity, velocity_multiplier]
        points.append([random() * 8, random() * 8, 0, 0, 0.9 + random() * 0.2])

def update(sense):
    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "middle":
            init(sense)
    gyro = sense.get_gyroscope()
    sense.clear()
    x_accel = G * sign(-sin(radians(gyro["pitch"] - zero_rotation["pitch"])))
    y_accel = G * sign(sin(radians(gyro["roll"] - zero_rotation["roll"])))
    for point in points:
        # Apply accelerations
        point[2] += x_accel * point[4]
        point[3] += y_accel * point[4]
        # Apply x-velocity
        point[0] += point[2]
        if point[0] < 0:
            point[0] = 0
            point[2] = 0
        if point[0] >= 8:
            point[0] = 7
            point[2] = 0
        # Apply y-velocity
        point[1] += point[3]
        if point[1] < 0:
            point[1] = 0
            point[3] = 0
        if point[1] >= 8:
            point[1] = 7
            point[3] = 0
        sense.set_pixel(int(point[0]), int(point[1]), 200, 200, 200)

init(sense)
while True:
    update(sense)
