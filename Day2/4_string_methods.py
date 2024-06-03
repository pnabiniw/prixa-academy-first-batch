# Methods are similar to function
print("Hello World")  # Here print() is a Built in function
a = "hello world"
x = a.capitalize()  # here capitalize() is a method
print(x)  # Hello world

x = a.upper()
print(x)  # HELLO WORLD

x = a.lower()
print(x)  # hello world

x = a.title()
print(x)  # Hello World

# split()
message = "Hello World I am learning Python"
result = message.split()
print(result)  # ["Hello", "World", "I", "am", "learning", "Python"]

result = message.split("e")
print(result)  # ["H", "llo World I am l", "arning Python"]


# join()
data = ["Hello", "World", "I", "am", "learning", "Python"]
result = " ".join(data)
print(result)  # Hello World I am learning Python
result = "+".join(data)
print(result)  # Hello+World+I+am+learning+Python

result = " + ".join(data)
print(result)  # Hello + World + I + am + learning + Python

print(result.title())
# result = data.join(" ")  # This is incorrect



# String Operations
# Concatenation
a = "Hello"
b = "World"
print(a + b)  # HelloWorld

# Membership operation
print("h" in "Hello")  # False
print("h".upper() in "Hello")  # True


# Repetition Operation
a = "Python"
print(a * 3)  # PythonPythonPython
print(a + 3)  # It raises error. + operator can be used with same datatypes

a = "1"
b = "2"
print(a + b)  # "12"
