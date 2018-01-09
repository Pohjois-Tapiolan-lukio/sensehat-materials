from sense_hat import SenseHat
from math import radians, sin, cos, sqrt

sense = SenseHat()

A = (130, 130, 130)
B = (170, 170, 170)
C = (20, 20, 20)
compass = [
    C,A,A,A,A,A,A,C,
    A,A,A,A,A,A,A,A,
    A,A,A,A,A,A,A,A,
    A,A,A,B,B,A,A,A,
    A,A,A,B,B,A,A,A,
    A,A,A,A,A,A,A,A,
    A,A,A,A,A,A,A,A,
    C,A,A,A,A,A,A,C,
]

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def clamp_pixel(n):
    return min(7, max(0, round(n)))

def draw_needle(sense, x, y, r, g, b):
    if abs(x) > abs(y):
        x = sign(x)
    elif abs(y) > abs(x):
        y = sign(y)
    for tail in range(3):
        draw_x = clamp_pixel(x * 3.5 + 3.5 - x * tail)
        draw_y = clamp_pixel(y * 3.5 + 3.5 - y * tail)
        sense.set_pixel(draw_x, draw_y, r, g, b)

while True:
    north = sense.get_compass()
    x = cos(radians(north))
    y = sin(radians(north))
    sense.set_pixels(compass)
    draw_needle(sense, x, y, 255, 128, 128)
    draw_needle(sense, -x, -y, 210, 210, 210)
