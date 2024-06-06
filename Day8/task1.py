# Create a student class with instance attribute name name and roll_number
# create classroom as class attribute and finally a method to get all his
# info.
# Finally print all his information

class Student:
    classroom = "Prixa Academy"

    def __init__(self, n, r):
        self.name = n
        self.roll = r

    def get_info(self):
        return f"Student name is {self.name}, roll is {self.roll} and academy
        is {self.classroom}"
    

s = Student("Jon", 21)
print(s.name)
print(s.roll)
print(s.classroom)
print(s.get_info())