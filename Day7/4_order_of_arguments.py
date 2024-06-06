# Order of function arguments
# The order must be:
# 1. Positional Arguments
# 2. Default / Keyword Arguments
# 3. *args
# 4. **kwargs


def message(a, b="World"):
    print(a + b)

# Variations while calling this function
message("Hello")
message("Hello", "Python")  # Hello Python
message(a="Hello", b="I am learning")  # Hello I am learning
message(b="I am learning", a="Hello")  # Hello I am learning

# message(b="I am learning", "Hello")  # This raises error


# def addition(**kwargs, *args):  This also raises error because *args should
# come first than **kwargs


    
def message(a, b, c, d=1, e=3, *args, **kwargs):
    print(a)  # 1
    print(b)  # 2
    print(c)  # 3
    print(d)  # 4
    print(e)  # 5
    print(args) # (6, 7, 8, 9)
    print(kwargs)  # {"x": 10, "y": 11, "z": 12}


message(1, 2, 3, 4, 5, 6, 7, 8, 9, x=10, y=11, z=12)
