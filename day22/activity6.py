'''
Three shapes: Circle, Rectangle, and Triangle.
Each can calculate its own area()
Write a single function print_area(shape) that can print the area of any 
shape object without checking its type.
'''
#Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2

#Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

#Triangle class
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

#print area of circle, rectangle, triangle
def print_area(shape):
    print("Area:", shape.area())

circle = Circle(6)
rectangle = Rectangle(2,9)
triangle = Triangle(5,6)

print_area(circle)
print_area(rectangle)
print_area(triangle)
