# range()
# range() is a built-in function in python which returs the range of numbers

a = list(range(10))
print(a)  # 0, 1, 2, 3, 4, 5, 6,7, 8, 9

b = list(range(5, 50))
print(b)  # 5, 6, 7, 8....49

c = list(range(5, 51, 2))
print(c)  # 5, 7, 9, 11, ....49


# WAP to find out even numbers in range 0 and 51

for i in range(51):
    if i % 2 == 0:
        print(i)

a = list(range(0, 51, 2))
print(a)


a = 0
while a <= 50:
    print(a)
    a = a + 2



# enumerate()
# enumerate() is also a built-in function which gives the elements of an iterable along with
# it's count

vowels = ["a", "e", "i", "o", "u"]
data = list(enumerate(vowels))
print(data)  # [(0, "a"), (1, "e"), (2, "i"), (3, "o"), (4, "u")]


for value in data:
    print(value)  # (0, "a")   (1, "e")


for index, value in data:
    print(index)  # 0
    print(value) # a


a = "Hello"
for each in a:
    print(each)  # H  e  l  l  o