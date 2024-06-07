import math

radius = float(input("Enter radius of the circle: "))
# Circumference of the circle = 2 pi r
circumference = 2 * math.pi * radius

print(f"circumference of the circle radius {round(radius)}cm is {round(circumference/1000)}m")
