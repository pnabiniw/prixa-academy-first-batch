# All those symbols which are used to carry out certain operations are called operators
# Python set of operators
# 1. Arithmetic Operators
# 2. Logical Operators
# 3. Relational / Comparison
# 4. Membership
# 5. Identity
# 6. Assignment

# Arithmetic Operators (+, -, /, *, //, %)
a = 1
b = 2
print(a + b)

print(a - b) 
print(a * b)
print(a / b)

# // is floor division in python

a = 5
print(a // 2)  # 2

# % is remainder operator
print(10 % 2)  # 0
print(10 % 3)  # 1




# Logical Operators
# "and", "or" and "not" are the logical operators
# Results of logical operators are boolean (True / False)

print(True and True)  # True
print(True and False) # False
print(False and True) # False
print(False and False) # False


print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

print(not True)  # False
print(not False)  # True


# Relational Operators
# >, <, >=, <=, !=, ==
# Result of relational operators is also a boolean

print(5 > 2)  # True
print(10 < 1)  # False
print(5 >= 5)  # True
print(6 <= 10)  # True
print(5 == 5)  # True
print(1 != 2)  # True


# Membership Operator
# "in" and "not in" are the membership operators
# Result of membership operation is also a boolean

print(2 in [1, 2, 3])  # True
print(5 not in [5, 6, 7])  # False
print(3 in [5, 6, 7])  # False
print(6 not in [1, 2, 3])  # True


# Identity Operator
# "is" and "is not" are the identity operators
# This operator can be compared with == , !=

# If both the objects have same memory location then "is" operator gives True
# If both the objects are in different memory location then "is" gives False
a = 1
b = 1
print(a == b)  # True
print(a is b)  # True

a = []
b = []
print(a is b)  # False
print(a == b) # True

# Assignment
# Basic assignment operator is "="
# It is used to store data in a variable

a = 1
a = a + 1
print(a)  # 2
a = a + 1
print(a)  # 3

a += 1  # this is same as a = a + 1
print(a)  # 4


a = a * 2
print(a)  # 8
a *= 2 # 16