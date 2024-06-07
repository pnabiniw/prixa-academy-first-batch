# Method Overriding
# It is possible in python to override the method of the
# parent class


class Person:
    def get_details(self):
        return "Hello World"
    
    def get_details(self):
        # return 
        return f"hello world"
    
class Employee(Person):
    def get_details(self):
        # return 
        return f"{super().get_details()}, I am learning python"
    
e = Employee()
print(e.get_details())


# Method / Function overloading
# Technically, function / method overloading is not possible in python
def addition(a, b):
    return a + b


def addition(a, b, c):
    return a + b + c


# r1 = addition(2, 3)  # Error
r2 = addition(1, 2, 3)

# print(r1)
print(r2)


def addition(a, b, c):
    return a + b + c


addition(1, 2)  # 3
addition(1, 2, 3)  # 6