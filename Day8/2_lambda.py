# lambda functions are the anonymous functions in python
# They are used in such cases where we have to pass function reference
# They are the one-liner function

# writing a lambda expression

# def add_ten(element):
#     return element + 10


# map()
data = [1, 2, 3, 4, 5]
# lambda element: element + 10

result = map(lambda element: element + 10, data)


# filter()
data = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda x: x % 2 == 0, data))
print(result)



data = [12, 10, 5, 6, 7, 20, 15]
def greater_than_ten(element):
    if element > 10:
        return True
    else:
        return False

result = filter(greater_than_ten, data)
print(result)  # [12, 15, 20]


from functools import reduce

data = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x * y , data)
print(result)  # 120
