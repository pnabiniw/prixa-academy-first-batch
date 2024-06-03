# Tuple being immutable it has only two methods

# count()
data = (1, 2, 3, 4, 5, 5, 1, 1, 2, 2)
result = data.count(2)
# result = data.count(7)  # Error
print(result)


# index()
data = ("a", "b", "c", "e", "d", "d", "a", "b")
result = data.index("b")
print(result)  # 1
a = (1, 2, 3, 4)
r = a.index(3)
print(r)  # 2

result = data.index("b", 4)
print(result)  # 7

RESULT = data.index("d", 2, 5)
print(RESULT) # 4


result = data.index("d", 5, 7)
print(result)  # 5

