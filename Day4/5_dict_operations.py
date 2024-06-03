# Membership Operation
items = {"one": "pen", "two": "pencil"}

print("one" in items)  # True
print("pen" in items)  # False


# Built-in functions
items = {"one": "pen", "two": "pencil"}
print(len(items))  # 2


items = {"one": 1, "two": 2, "three": 3}
r = sum(items.values())
print(r)  # 6


r = sorted(items.values(), reverse=True)
print(r) # [3, 2, 1]
