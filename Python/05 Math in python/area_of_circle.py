import math

radius = float(input("Enter radius of the circle: "))
# Area of the circle = 2 pi r
area = math.pi * pow(radius, 2)

print(f"area of the circle radius {round(radius)}cm is {round(area, 2)}cm^2")
