# Loops are used in programming to run the tasks repeatedly
# There are two types of loops in Python
    # 1. for loop
    # 2. while loop

# 1. for loop
# For loops are used in iterables (sequential data like list, 
# tuple, string, dictionary, set)

vowels = ["a", "e", "i", "o", "u"]
for vowel in vowels:
    print(vowel)

fruits = ["apple", "mango", "orange", "pineapple"]
for a in fruits:
    print(a)


# 2. While loops
# While loops are used with truthy or falsy statement
# The loop is executed until the condition is truthy

a = 0
while a <= 10:
    print(a)
    a = a + 1

a = 0
while a <= 10:
    print(a)
    a = a + 1

# To create infinite loop we can use True
while True:  # Infinite loop
    print("Hello World")
