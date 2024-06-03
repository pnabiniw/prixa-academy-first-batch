# append()
a = [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]

# extend()
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)  # [1, 2, 3, 4, 5, 6]

# remove()
a = ["a", "b", "c", "d"]
a.remove("c")
a.remove("x") # Error
print(a)  # ["a", "b", "d"]

# pop()
data = ["a", "b", "c", "d"]
result = data.pop()
print(result)  # d
print(data)  # ["a", "b", "c"]
result = data.pop(1)
print(data)  # ["a", "c"]
print(result)  # b


# insert()
data = ["a", "b", "c", "d"]
data.insert(1, "I")
print(data) # ["a", "I", "b", "c", "d"]


# clear()
data = ["a", "b", "c", "d"]
data.clear()
print(data)  # []

# copy()
a = [1, 2, 3]
b = a  # Pass by reference
a.append(4)
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]

b = a.copy()  # Pass by value
a.append(5)
print(a) # [1, 2, 3, 4, 5]
print(b)  # [1, 2, 3, 4]



# sort()
data = [5, 1, 40, 100, 2, 10]
data.sort()
print(data)  # [1, 2, 5, 10, 40, 100]

data.sort(reverse=True)
print(data)  # [100, 40, 10, 5, 2, 1]


# reverse()
data = [5, 1, 40, 100, 2, 10]
data.reverse()
print(data)  # [10, 2, 100, 40, 1, 5]

