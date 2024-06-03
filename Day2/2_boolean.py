# Boolean are immutable datatypes in python
# True and False are the boolean types in python
# True and False are also the keywords to represent boolean values

a = True
print(a) # True
b = False
print(b)  # False


# Concept of Truthy and Falsy in python
# Falsy
# All those datatypes in python which are empty or 0 / 0.0 or None or False
# itself, these are falsy

print(bool(0))
a = 0
b = 0.0
c = []
d = ""
e = ()
f = {}
g = set()
h = None
i = False


# Truthy
# All those none empty datatypes including True itself are truthy datatypes
a = 1
b = -5
c = 2.2
d = ["1", 2]
e = (3, 4)
f = {"name": "Jon", "age": 21}
g = {1, 2}
h = "Python"
i = True

if 5 > 2:
    print("5 is greater")

if [1, 2, 3]:
    print("The list is not empty")

if []:
    print("The list is empty")


# Boolean is the subclass of integer datatype
# We can use True as 1 and False as 0 in python
a = True + 5
print(a)  # 6
b = True + True
print(b) # 2
print(False * 2)  # 0


# Operations that give boolean results
# 1. Logical Operations
print(True or False)  # True
print(True and False)  # False
print(not 3)  # False
print(not False) # True

# 2. Relational / Comparison Operations
# >, <, >=, <=, ==, !=
print(5 > 2)  # True
print(5>2 and 10 < 3)  # False


# 3. Membership Operations
print(3 in [1, 2, 3])  # True
print(5 not in (5, 7, 8))  # False
print("hello" in {"Hello", "World"})  # False


# 4. Identity Operation
a = 1
b = 1
print(a is b) # True

a = []
b = []
print(a is b)  # False
print(a == b)  # True
print(a != b)  # False

a = None
print(a is None)  # True

