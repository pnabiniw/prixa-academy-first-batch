student = {"name": "Hary", "age": 30, "address": "KTM"}

# update()
# get()

# keys
keys = student.keys()
print(keys)  # dict_keys(["name", "age", "address"])
keys = list(keys)


# values
values = student.values()
print(values)  # dict_values(["Hary", 30", "KTM"])

# items
items = student.items()
print(items)  # dict_items([("name", "Hary"), ("age", 30), ("address", "KTM")])

items = list(items)  # [("name", "Hary"), ("age", 30), ("address", "KTM")]

a, b = items[0]  # "name", "Hary"
print(a)  # name
print(b)  # Hary
