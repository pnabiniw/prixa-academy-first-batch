# WAP to input a number and check whether the number is odd or even

num = int(input("Enter a number "))

remainder = num % 2
if remainder == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# WAP to input three numbers and find the greatest among three
num1 = int(input("Enter a number "))
num2 = int(input("Enter second number "))
num3 = int(input("Enter third number "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the greatest")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the greatest")
else:
    print(f"{num3} is the greatest")

