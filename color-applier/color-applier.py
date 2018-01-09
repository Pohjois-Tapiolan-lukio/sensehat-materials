from sense_hat import SenseHat

sense = SenseHat()

def apply_color(r, g, b):
    global sense
    pixel_list = [(r, g, b) for i in range(64)]
    sense.set_pixels(pixel_list)

print("Värin punaisuus (0-255):")
r = int(input())
print("Värin vihreys (0-255):")
g = int(input())
print("Värin sinisyys (0-255):")
b = int(input())
apply_color(r, g, b)
