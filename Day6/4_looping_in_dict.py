student = {"name": "Jon", "age": 30, "address": "KTM"}


for each in student:
    print(each)  # name   age   address

for key, value in student.items():
    print(key)  # name  age  address
    print(value) # Jon  30   KTM


for each in student.values():
    print(each)  # Jon  30  KTM