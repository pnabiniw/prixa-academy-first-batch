# Conditions are the statement which are used to make decisions in 
# programming

a = 5
b = 2
if a > b:
    print("a is greater")

if b:
    print("b is non-zero")

# Variations in conditional statement

#1. Simple if
a = 5
b = 2
if a > b:
    print("a is greater")

# if...else statement
a = 5
b = 7
if a > b:
    print("a is greater")
else:
    print("b is greater")


# if...elif...else statement
if a > b:
    print("a is greater")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater")


# if...elif ladder
a = 5
b = 2
c = 1
if a > b:
    print("a is greater")
elif a == b:
    print("a and b are equal")
elif a == c:
    print("a and c are equal")
else:
    print("b is greater")


# Nested If statement
a = 5
b = 2
c = 1
if a > b:
    if a > c:
        print("a is the greatest")
    else:
        print("a is second greatest")
elif b > c:
    if b > a:
        print("b is the greatest")
    else:
        print("b is the second greatest")


# ternary if
a = 1
b = 2
print("a is greater than b") if a > b else print("b is greater than a")  # ternary if

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")


a = 1
b = 2
c = 3

if c > a:
    print("c is greater than a")
if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")



if c > a:
    print("c is greater than a")
elif b > a:
    print("b is greater than a")
else:
    print("a is greater than b")