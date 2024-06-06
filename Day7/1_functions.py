# FUnctions are the block of reusable code which may take input, do some processing and 
# finally return output
# We use "def" keyword to create a function in python

# Types of functions
#1. Built-in functions (e.g. print(), type(), help(), sum(), sorted(), reversed() etc.)
# 2. User-defined functions

# Creating a function in python
def addition(a, b):  # Function Definition
    c = a + b
    return c


result1 = addition(2, 3)  # Function Call
result2 = addition(6, 7)  # Function Call
print(result1) # 5
print(result2) # 5

# Variations in python function
# 1. With parameters / arguments and with return
def addition(a, b):  # Function Definition
    c = a + b
    return c

r = addition(4, 5)
print(r)  # 9


# 2. With parameters without return
def addition(a, b):
    print(a + b)

result = addition(2, 3)
print(result)  # None

a = [3, 4, 5]
result = a.append(7)
print(result)  # None
print(a)  # [3, 4, 5, 7]


# 3. Without parameter, with return
def message():
    return "Hello World"

result = message()
print(result)  # Hello World


# 4. Without parameter, without return
def message():
    print("Hello World")

result = message()
print(result)  # None


# If a function doesn't return anything then it returns None by default
# We can also simply write "return" to return None

def addition(a, b):
    print(a + b)
    return
