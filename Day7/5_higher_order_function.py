# If a function takes another function as an argument then such a function 
# is called higher order function
# In python map(), reduce(), filter(), decorators etc. are the higher order
# function

# map()
# map() function takes first argument as a function and second argument as iterbale

a = [1, 2, 3, 4]
result = []
for i in a:
    result.append(i+10)


print(result)  # [11, 12, 13, 14]

# Using map() function
def add_ten(element):
    return element + 10

result = map(add_ten, a)
print(list(result))  # [11, 12, 13, 14]
