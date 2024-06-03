# Dictionary is a mutable datatype in Python
# It is a combination of key and value pair separated by commas and
# enclosed within curly braces

# Creating non-empty dictionary
student = {"name": "Jon", "age": 24, "address": "KTM"}
student = dict(name="Jon", age=24, address="KTM")

# Creating an emplt dictionary
a = {}
b = dict()


# Adding and removing dictionary items
student = {"name": "Jon", "age": 24, "address": "KTM"}
student["roll"] = 12
print(student)  # {"name": "Jon", "age": 24, "address": "KTM", "roll": 12}

student.update(email="jon@email.com")
print(student)  # {"name": "Jon", "age": 24, "address": "KTM", "roll": 12, "email": "jon@email.com"}


student = {"name": "Jon", "age": 24}
student.update({"email": "jon@email.com", "address": "KTM"})
print(student)  # {"name": "Jon", "age": 24, "address": "KTM", "email": "jon@email.com"}


result = student.pop("name")
print(result)  # Jon
# result = student.pop("roll")  # Error
result = student.pop("roll", 20)  # None
print(result)  # None
print(student)  # {"age": 24, "address": "KTM", "email": "jon@email.com"}


student = {"name": "Jon", "age": 24, "address": "Pokhara"}
print(student)
result = student.pop("name", "Jane")
address = student.pop("address", "Bhaktapur")
print(result)  # Jon
print(student)  # {"age": 24}
print(address)  # Pokhara

student.clear()
print(student)  # {}



# Accessing dicitionay items
student = {"name": "Mane", "age": 20, "address": "KTM"}
age = student["age"]
print(age)  # 20

roll = student["roll"] 
print(roll) # KeyError

name = student.get("name")
print(name)  # Jon

roll = student.get("roll")
print(roll)  # None

roll = student.get("roll", 21)
print(roll)  # 21

name = student.get("name", "Jane")
print(name)  # Mane


# Rules for creating dictionary keys and values

# Dictionary Values can be any datatype (both mutable and immutable)
# But, dictionary keys can only be immutabe datatypes


student = {"names": ["Jon", "Jane", "Hary"], }
data = {1: "Ram", 10: "Hari"}
print(data[10])  # Hari


# data = {[1, 2]: 1.1}  # Error
# print(data)  # 

data = {(1, 2): (1, 2)}
print(data)  # Valid

data = {(1, 2, [1, 2]): [1, 2]}
print(data)  # InValid