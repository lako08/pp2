class Shape:
    def area(self):
        return 0
    
    def description(self):
        return "This is a shape"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def description(self):
        return f"This is a circle with radius {self.radius}"

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def description(self):
        return f"This is a square with side {self.side}"

shapes = [Circle(5), Square(4), Shape()]
for shape in shapes:
    print(shape.description())
    print(f"Area: {shape.area()}")