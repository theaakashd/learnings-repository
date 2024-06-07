# Degree symbol in win: alt + 0176 = 12
unit = input("Is this temp in Celsius or Fahrenheit (C or F): ")
temp = float(input("Enter your temp: "))

if unit == "F":
    CTemp = (temp - 32) * 5/9
    print(f"{temp} degree fahrenheit is equal to {CTemp} degree celsius")
elif unit == "C":
    FTemp = temp * (9/5) + 32
    print(f"{temp} degree celsius is equal to {FTemp} degree fahrenheit")
else:
    print(f"{unit} is not valid unit of measurement")