name = "akash"
age = 21
gpa = 1.9
student = True

# typecasting - explicit casting
age = float(age)
gpa = int(gpa)
student = str(student)

print("name: ", type(name))
print("age: ", type(age))
print("gpa: ", type(gpa))
print("student: ", type(student))

# Implicit typecasting
x = 2
y = 2.0

x = x / y

print(x)