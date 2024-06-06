# *args, and **kwargs are the function arbitrary arguments
# *args is like an expandable bucket which can take arbitrary number of values

def addition(*args):
    print(args)
    print(type(args))  # tuple
    print(sum(args))
    for each in args:
        print(each)


addition(1, 2)  # 3
addition(1, 2, 3)  # 6
addition(1, 2, 3, 4)  # 10
addition(1, 2, 3, 4, 5)  # 15


def addition(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(sum(kwargs.values()))


addition(a=1, b=2)  # 3
addition(a=1, b=2, c=3) # 6
addition(a=1, b=2, c=3, d=4) # 10
addition(a=1, b=2, c=3, d=4, e=5)  # 15


# Dict keys must be immutable
# Dict values can br any datatype

def addition(*args, **kwargs):
    print(args)  # (2, 10, 2, 4)
    print(kwargs) # {"a": 5, "b": 9, "c": 11, "d": [1, 2, 3]}


addition(2, 10, 3, 4, a=5, b=9, c=11, d=[1, 2, 3])
