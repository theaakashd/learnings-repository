# Python Data Structures

| No  | Topics                                  |
| --- | --------------------------------------- |
| 1   | [Lists and Tuples](#1-lists-and-tuples) |
| 2   | [Sets](#2-sets)                         |
| 3   | Dictionaries                            |

## 1. Lists and Tuples

-   These are called `Compound Data Types`

### **Tuples**

-   Tuples are an ordered sequence
-   Here is a Tuple Ratings
-   Tuples are written as comma-separated elements within parentheses

```python
Ratings = (10, 9, 6, 5, 10, 8, 9, 6 ,2)
```

-   In python we have data type such as - string(str), integer(int), float
-   A tuple can hold multiple types `tuple1 = ('akash', 10, 1.2)`
-   But the type of `tuple1` will be tuple.
-   Each tuple can be acess using index.

```python
tuple1[0] # 'akash'
type(tuple1) # tuple
```

-   Concatenation in tuples
-   If we want multiple elements from tuple we can use `Slicing method`

```python
Ratings = (10, 9, 6, 5, 10, 8, 9, 6 ,2)
Ratings2 = ("akash", 1.1, 4.6, "elza")

Final = Ratings + Ratings2
print(Final)
start = len(Ratings)
end = len(Final)
print(Final[start:end])
type(Final)
# output:
(10, 9, 6, 5, 10, 8, 9, 6, 2, 'akash', 1.1, 4.6, 'elza')
('akash', 1.1, 4.6, 'elza')
tuple
```

-   Tuples are Immutable means we can't change them
-   So if we want new tuple we have to use new variable to hold the value

```python
Tuple = (10, 9, 6, 5, 10, 8, 9, 6 ,2)
sorted_tuple = sorted(Tuple)
print(sorted_tuple)

# output:
[2, 5, 6, 6, 8, 9, 9, 10, 10]
```

### **Nesting**

-   Nesting is more complex data structure
-   It's like having tuples inside a tuple

```python
NT = (1,2, ("pop", "rock"), (3,4), ("disco", (1,2)))
print(NT[-1])
print(NT[-1][0])
print(NT[-1][-1][1])

# output:
('disco', (1, 2))
disco
2
```

### **Lists**

-   Lists are also ordered sequence
-   Here is a List `L`
-   A List is represented with square brackets (arrays if you know JavaScript)
-   List are like tuples but they are `mutable`
-   In list you can use nest all data types but also data structures like tuples.
-   Same index is used to access nesting
-   We concatenate two lists by adding them but it's mutable so we can just use `extend()` method also.

```python
L = ["Akash Debnath", 10.1, 1999, [1,2], ('A', 1)]
L.extend(["akash"])
L[0] = "Elza"
print(L[-1])
print(L[-1][0])
print(L[3:len(L)])
print(L)

# output:
elza
e
[[1, 2], ('A', 1), 'elza']
['Elza', 10.1, 1999, [1, 2], ('A', 1), 'akash']
```

-   We can delete an element from list by using `del()`

```python
L = ["Akash Debnath", 10.1, 1999, [1,2], ('A', 1)]
del(L[0])
print(L)

# output:
[10.1, 1999, [1, 2], ('A', 1)]
```

-   We can convert a string to list using `split()`

```python
"akash debnath".split()

# output:
['akash', 'debnath']
```

-   We can use `split()` separate strings on a specific character known as a delimeter.

```python
"A,B,C,D".split(",")

# output:
['A', 'B', 'C', 'D']
```

-   Multiple name referencing the same object is known as `Aliasing`

```python
obj = [10, 5, 6]
A = obj
B = obj
A[0] = 99
print(f"A: {A}")
print(f"B: {B}")

#output:
A: [99, 5, 6]
B: [99, 5, 6]
```

-   You can clone list A by following this syntax: `B=A[:]`
-   By doing this the Value of B won't change when you change the value in A.

```python
obj = [10, 5, 6]
A = obj
B = A[:]
A[0] = 99
print(f"A: {A}")
print(f"B: {B}")

# output
A: [99, 5, 6]
B: [10, 5, 6]
```

-   To get more help in python with tuples or lists or any data structure run this

```python
# help(object or data type name)
help(tuple)
help(list)
```

### 2. **Sets**

-   **Sets are a type of collection** <br>
    This means that like lists and tuples you can input different Python types.
-   **Unlike lists and tuples they are unordered** <br>
    This means sets do not record element position
-   **Sets only have unique elements** <br>
    This means there is only one of a particular element in a set

example of a set

```python
# as you can see there are duplicate items in this set
set1 = {"pop", "rock", "soul", "pop", "rock"}

# when the set get created this is how it looks
# no duplicates
set1 = {"pop", "rock", "soul"}
```

-   You can convert a `LIST` to `SET` using function `set()` this is called type casting.
-   You give `LIST` as a input to `SET` which converts it into set and returns it.

example:

```python
List = [1,2,3,4,5,1,2,1,1,4,5]
ConvertedList = set(List)
print(ConvertedList)
print(type(ConvertedList))

# output:
{1, 2, 3, 4, 5}
<class 'set'>
```
