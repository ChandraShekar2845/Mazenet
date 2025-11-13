PI = 3.14
class Shape():
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * (self.radius ** 2)
    def perimeter(self):
        return 2 * PI * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
circle1 = Circle(5)
rectangle1 = Rectangle(4, 6)

print("Circle:")
print("Area:", circle1.area())
print("Perimeter:", circle1.perimeter())

print("Rectangle:")
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())

