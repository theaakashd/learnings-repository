# logical operator = used on conditional statements

# and = checks two or more conditions if True
# or = checks if at least one condition is True
# not = True if condition is False, and False if the condition is True

temp = -18
sunny = True

if temp <= 0 or temp >= 30:
    print("good")
else:
    print("bad")

if not sunny:
    print("hot outside")
else:
    print("cloudy")
