class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def __add__(self, other):
        return self.radius + other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius


c1 = Circle(5)
c2 = Circle(10)
x = c1.radius + c2.radius
print(x)  # 15


result = c1 + c2
print(result)  # 15

print(c1 > c2)  # False