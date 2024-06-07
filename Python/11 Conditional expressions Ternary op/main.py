# conditional expression
# A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition
# X if condition else Y
# x > 5 ? "positive" : "negative" (This is in javascript)

x = 10
a = 6
b = 7
age = 18
temp = 20
user_role = "admin"
isAdmin = False

print(f"positive" if x >= 5 else "negative")
result = "even" if x % 2 == 0 else "odd"
max_num = a if a > b else b
min_num = a if a < b else b
status = "adult" if age >= 18 else "kid"
weather = "hot" if temp > 20 else "cold"
user_status = "admin" if user_role == "admin" else "user"
user_statuss = "admin" if isAdmin else "user"

print(f"result: {result}")
print(f"max_num: {max_num}")
print(f"min_num: {min_num}")
print(f"age_status: {status}")
print(f"weather: {weather}")
print(f"user_status: {user_status}")
print(f"isAdmin: {user_statuss}")
