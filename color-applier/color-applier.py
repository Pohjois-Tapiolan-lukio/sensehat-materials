from sense_hat import SenseHat

sense = SenseHat()

print("Värin punaisuus (0-255):")
r = int(input())
print("Värin vihreys (0-255):")
g = int(input())
print("Värin sinisyys (0-255):")
b = int(input())
color = (r, g, b)
sense.clear(color)
