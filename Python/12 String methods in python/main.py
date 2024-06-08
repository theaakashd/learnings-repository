# String methods

# len(name) : gives you the length of the given string
# The count start from the beginning of the string
# name.find("") : returns the first occurrence of the given character or the position
# name.rfind("") : returns the last occurrence of the given character or the position
# find() & rfind() : method will return -1 if there's no result
# capitalize() : will return a string will capitalize first letter
# upper() : will return a uppercase string
# lower() : will return a lowercase string
# isdigit() : only returns True if the string is all digits
# isalpha() : only returns True if the string only contains alphabets, False if string has any space also
# count("-") : will count how many times "-" will occur in the string.
# replace("-","*") : will replace all occur of "-" with "*" in the given string
# hash(name) : will return the hash value of the name variable
# help(str) : Which will show all the methods available for the datatype

# name = input("Enter your full name: ")
name = "akash debnath"
name2 = "ROXY"
name3 = "152151351"
phone_number = "123-456-7890"
myname = "akashdebnath"


length = len(name)
first_occur = name.find(" ")
last_occur = name.rfind("h")
capitalize = name.capitalize()
upper = name.upper()
lower = name2.lower()
isDigit = name3.isdigit()
isAlpha = name.isalpha()
phoneNumber = phone_number.count("-")
string = name.replace('a', 'x')
checkspace = myname.find(" ")


print(f"length: {length}")
print(f"first_occur: {first_occur}")
print(f"last_occur: {last_occur}")
print(f"capitalize: {capitalize}")
print(f"upper: {upper}")
print(f"lower: {lower}")
print(f"isDigit: {isDigit}")
print(f"isAlpha: {isAlpha}")
print(f"count: {phoneNumber}")
print(f"replace: {string}")
print(f"checkspace: {checkspace}")
# print(help(str))
