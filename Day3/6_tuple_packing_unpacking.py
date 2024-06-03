a = 1
print(type(a))  # int
a = 1,  # This is tuple packing
a = "hello",
print(type(a))  # Tuple

a = 1, 2, 3
print(a)  # (1, 2, 3)
print(type(a))  # Tuple


a, b = 1, 2
print(a)  # 1
print(b)  # 2

# a, b, c = 1, 2 # This raises error
# a, b = 1, 2, 3 # This also raises error


a = 1
b = 2

c = a
a = b
b = c


print(b)  # 1
print(a)  # 2


x = 11
y = 12

x, y = y, x
print(x)  # 12
print(y)  # 11
