### Strings Operations

-   String operations using index to get the character.

```python
name = "Akash Debnath"
print(f"letter at position 1: {name[0]}") // A
print(f"letter at position 2: {name[1]}") // k
print(f"letter at position last: {name[-1]}") // h
print(f"letter at position 2nd last: {name[-2]}") // t
```

-   When we do `name[0:3]` it means start from `0` index up-to index `3` but don't count the index `3`.

```python
name = "Akash Debnath"
print(name[0:3]) // Aka
```

-   First character and then from there only choose the 2nd one.

```python
name = "Akash Debnath"
print(name[::2]) // AahDbah
```

-   Every 2nd character up-to index 5.

```python
name = "Akash Debnath"
print(name[0:5:2]) // Aah
```

-   To get the length of the string.

```python
name = "Akash Debnath"
print(len(name)) // 13
```

-   This is called string concatenation

```python
name = "Akash Debnath"
statement = " is the best!"
print(name + statement) // Akash Debnath is the best!
```

-   Tuples
-   Duplicates the strings 3 times
-   we can't change the value of the string but can create new string
-   strings are `immutable` means we can't change it once we declare.

```python
name = "Akash Debnath "
print(3 * name)

// Akash Debnath Akash Debnath Akash Debnath
```

-   `\` are meant to proceed escape sequences
-   escape sequences are strings that are difficult to input

```python
print("Akash \nDebnath")
print("Akash \tDebnath")
print("Akash \\ Debnath") // Akash \ Debnath
```

-   back slash n `\n` represent new line.
-   back slash t `\t` represent a tab.
-   `\\` if you want a back slash to show in your string.
