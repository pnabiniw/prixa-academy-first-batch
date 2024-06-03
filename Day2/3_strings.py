# Strings are immutable datatypes in Python
# They are the sequence of characters enclosed in single(''), double ("")
# or triple quotes ("""  """)/('''    ''')

# Creating non-empty strings
message = "hello"
print(message)  # hello
message = 'Python'
message = """
Hello World. I am learning
Python
"""
print(message)  # 
a = str([1, 2, 3])
print(a)  # '[1, 2, 3]'

# Creating empty strings
a = ""
b = ''
c = """"""
d = str()


### Accessing string elements ####
# String elements can be accessed using indexing and slicing

# Indexing
# Insexing always starts from 0 position
# To use indexing, we should use big brackets
data = "Prixa Academy"
print(data[0])  # P
print(data[4])  # a
print(data[-1])  # y
print(data[-1] == data[12])  # True
print(data[-5])  # a

print()
data[0]
# print(), type(), help()

# Slicing
# Slicing gives the substring from the main string
# For slicing we use [:]
# Slicing doesnt change the existing string, rather it gives a new string
data = "Prixa Academy. I am learning Python"
print(data[3:8])  # xa Ac
print(data[0:9])  # Prixa Aca

x = data[0:9]
print(x)  # Prixa Aca
print(data)  # "Prixa Academy. I am learning Python"

print(data[5:3])  # ""
print(data[10:2])  # ""


print(data[-8:-2])  # g Pyth
print(data[-10:-1])  # ing Pytho
print(data[-1:-10])  # ""

print(data[2:10:2])  # iaAa

