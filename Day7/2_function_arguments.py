# The input to a function are called arguments / parameters
# If it is used in function definition, we call it parameter
# The values passed to a function during function call are called arguments

# Type of arguments in python
# 1. Positional Argument
# 2. Default Argument
# 3. Arbitrary Argument

# 1. Positional Arguments
# They are compulsury arguments of a function

def addition(a, b, c):  # Here a, b, and c are positional arguments
    result = a + b
    return result

result = addition(1, 2, 3)
print(result)


# 2. Default Arguments
# Default arguments have some default value assigned to it which is used 
# only if the value is not passed during the function call.

def addition(a, b, c=10):
    result = a + b + c
    return result

result1 = addition(1, 2)
print(result1)  # 13

result2 = addition(1, 2, 3)
print(result2)  # 6

student = {"name": "Rahul", "age": 30}

name = student.get("name")
print(name)  # Rahul

name = student.get("name", "Rohan")
print(name)  # Rahul

