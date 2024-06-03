# Tuples are immutable datatypes in python
# They are the sequence of elements enclosed within small brackets 

# Creating non-empty tuples
a = (1, 2, 3)  # Tuple of integers
b = ("a", "b", "c")  # Tuple of strings
c = (1, "a", [3, 4], (5, 6), {"a": 1})
d = tuple([1, 2, 3])
print(d)  # (1, 2, 3)

# Creating empty tuple
a = ()
b = tuple()
print(a == b)  # True
print(a is b)  # True


# Accessing tuple elements
# Tuple elements can be accessed by indexing and slicing same as list and string
vowels = ("a", "e", "i", "o", "u")
print(vowels[0])  # a
print(vowels[4])  # u
# print(vowels[10])  # Error
print(vowels[-1])  # u
print(vowels[-4]) # e
# print(vowels[-100])  # Error


# Slicing
data = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
print(data[0:8])  # ("a", "b", "c", "d", "e", "f", "g", "h")
print(data[2:7]) # ("c", "d", "e", "f", "g")
print(data[7:3])  # ()
print(data[4:9]) # "e", "f", "g", "h", "i"
print(data[5:])  # "f", "g", "h", "i", "j"
print(data[:5])  # "a", "b", "c", "d", "e"

print(data[-9:-2])  # "b", "c", "d", "e", "f", "g", "h"
print(data[-2: -8])  # ()
print(data[-3:]) # "h", "i", "j"
print(data[:-2]) # "a", "b", "c", "d", "e", "f", "g", "h"

