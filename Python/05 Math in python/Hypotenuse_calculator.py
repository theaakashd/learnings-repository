import math
# Hypotenuse_calculator
# c = square root of a square + b square

a = float(input("Enter a: "))
b = float(input("Enter b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Hypotenuse value of {a} & {b} is: {round(c, 2)}")