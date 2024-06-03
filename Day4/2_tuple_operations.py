# Tuple concatenation
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print(c)  # (1, 2, 3, 4, 5, 6)


# Repetition Operation
a = (1, 2)
b = a * 3
print(b)  # (1, 2, 1, 2, 1, 2)


# Membership Operation
print("a" in ("b", "c", "a")) # True
print("z" in ("b", "c", "a")) # False
print("z" not in ("b", "c", "a")) # True 
print("a" not in ("b", "c", "a")) # False 
