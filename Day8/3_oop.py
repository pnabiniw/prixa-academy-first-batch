# OOP stands for Object Oriented Programming
# It is a programming paradigm where problems are break down into classes and objects
# Classes are the blueprint of object

# We use "class" keyword to make a class in Python
# User-defined classes should be in PascalCase
# StudentInformation => PascalCase
# studentInformation => camelCase
# student_information => snake_case

# class Student:
#     pass

# class StudentInformation:
#     pass

# class, object / instance, class attribute, instance attribute, constructor

class Vehicle:
    engine_type = "Petrol"  # class attribute

    def __init__(self, color, company):  # constructor
        self.color = color  # instance attribute
        self.company = company  # instance attribute

    def get_info(self):
        return f"color of the vehicle is {self.color} and company is {self.company}"

    

v1 = Vehicle("red", "yamaha")
v2 = Vehicle("blue", "suzzuki")
# Here v1 is Vehicle object / instance
# We can access class attributes by using . operator

print(v1.engine_type)  # Petrol

print(Vehicle.engine_type)  # Petrol
print(v1.color)  # red
print(v1.company)  # yamaha


print(v2.color)  # blue
print(v2.company)  # suzzuki


# v1 = Vehicle()  # Vehicle object
a = list()  # List object
l = [1, 2, 3]  # Here you are creating list object
# l.append()

sum([1, 2, 4])


result = v1.get_info()
print(result)