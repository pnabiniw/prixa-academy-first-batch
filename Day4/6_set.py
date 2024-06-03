# Set is a mutable datatype in python
# But set elements must be immutable
# They are the sequence of non-repeated elements enclosed within curly braces
# Sets are unordered. Order doesn't matter in sets
# Collection of well-defined items

# Creating non-empty set
vowels = {"a", "e", "i", "o", "u"}
data = {1, 1, 2, 2, 3, 3}
print(data)  # {1, 2, 3}


a = [1, 2]
b = [2, 1]
print(a == b)  # False

a = {2, 1}
b = {1, 2}
print(a == b) # True

# Creating an empty set
a = set()
# b = {}  # This is not an empty set. This is empty dictionary

# Set elements can't be accessed by using indexing and slicing because they are unordered
# If you want to access set elelments then you need to typecast to other datatype
a = {2, 1}
a = list(a)


# Set methods
# discard()
a = {"a", "b", "c"}
a.discard("c")
print(a)  # {"a", "b"}
a.discard("x")  # It doesn't raise error

# remove()
a = {"a", "b", "c"}
a.remove("b")
print(a)  # {"a", "c"}
# a.remove("d") # It raises error

# clear()
a.clear()
print(a)  # set()


# union()
a = {1, 2, 3}
b = {4, 5, 6}
result = a.union(b)
print(result)

result = a | b
print(result)  # {1, 2, 3, 4, 5, 6}

# intersection()
# a.intersection_update()
a = {1, 2, 3}
b = {3, 4, 5}
result = a.intersection(b)
print(result)  # {3}

result = a & b
print(result)  # {3}


# difference()
# a.difference_update()
a = {1, 2, 3, 4}
b = {4,5 ,6, 7}
result = a.difference(b)
print(result)  # 1, 2, 3
result = a - b
print(result)


# symmetric_difference()
a = {1, 2, 3, 4}
b = {4,5 ,6, 7}
result = a.symmetric_difference(b)
print(result)  # {1, 2, 3, 5, 6, 7}

result = a ^ b
print(result)  # {1, 2, 3, 5, 6, 7}


# symmetric_difference_update
a = {1, 2, 3, 4}
b = {4,5 ,6, 7}
a.symmetric_difference_update(b)
print(a)  # {1, 2, 3, 5, 6, 7}