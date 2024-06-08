# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = "akash"

if len(username) > 12:
    print("username must be under 12 characters.")
elif not username.isalpha():
    print("username must not contain any digits or spaces")
else:
    print("Username created!")
