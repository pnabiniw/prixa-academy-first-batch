# Concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # [1, 2, 3, 4, 5, 6]


# Repetition Operation / Broadcast operation
a = [1, 2]
print(a*2)  # [1, 2, 1, 2]


# Membership Operation
print(2 in [1, 2, 3]) # True
print(5 not in [4, 5, 6])  # False


# Some built-in functions which can take list as argument4

# len()
b = [4, 5, 6]
result = len(b)
print(result)  # 3
result = len("Python")
print(result)  # 6


# sum()
b = [1, 2, 3]
result = sum(b)
print(result)  # 6


# sorted()
a = [10, 100, 2, 1, 5, 40]
result = sorted(a)
print(result)  # [1, 2, 5, 10, 40, 100]

result = sorted(a, reverse=True)
print(result)  # [100, 40, 10, 5, 2, 1]
