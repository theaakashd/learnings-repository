# indexing = accessing elements of a sequence using [] (indexing operator)
# [start : end : step]
# remember index counting starts from 0 not 1
# string[::-1] : reverse the string

string = "a brown fox jumps over the lazy dog."

a = string[0]
# start 0th position & end 7th position
b = string[0:7]
# if the starting is 0 no need to mention it this will work too
c = string[:7]
d = string[8:11]
# from 12th index to everything till end of the string.
e = string[12:]
f = string[-4]
# starting from 0th index and print every 2 step
g = string[::2]

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")
print(f"f: {f}")
print(f"g: {g}")

# outputs
# a: a
# b: a brown
# c: a brown
# d: fox
# e: jumps over the lazy dog.
# f: d
# g: abonfxjmsoe h aydg
