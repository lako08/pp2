class Flyer:
    def fly(self):
        return "Flying high!"

class Swimmer:
    def swim(self):
        return "Swimming deep!"

class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return "Quack!"

class Walker:
    def walk(self):
        return "Walking..."

class Runner:
    def run(self):
        return "Running fast!"

class Athlete(Walker, Runner):
    def __init__(self, name):
        self.name = name
    
    def exercise(self):
        return f"{self.name} is exercising"

duck = Duck("Donald")
print(duck.fly())
print(duck.swim())
print(duck.make_sound())

athlete = Athlete("Usain")
print(athlete.walk())
print(athlete.run())
print(athlete.exercise())