class Person:
    def __init__(self, name, age):
        self.name = name  # p.name = Jane   p.age = 30
        self.age = age

    def get_details(self):
        print(f"Name of the student is {self.name} and age of the student is {self.age}")


# p = Person("Jane", 30)
# print(p.get_details())  # None


class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):
        print(super().get_details())
        return f"Salary is {self.salary} designation is {self.designation}"

emp = Employee("Hary", 31, 12000, "Manager")
print(emp.get_details())

p2 = Person("Jon", 21, 12000, "Manager")
p2.get_details()