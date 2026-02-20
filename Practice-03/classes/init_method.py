class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person1.introduce()
person2.introduce()

rect = Rectangle(5, 3)
print(rect.area())