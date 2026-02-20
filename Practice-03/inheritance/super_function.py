class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"Vehicle: {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def info(self):
        return f"{super().info()}, Doors: {self.doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type
    
    def info(self):
        return f"{super().info()}, Type: {self.type}"

car = Car("Toyota", "Camry", 4)
moto = Motorcycle("Harley", "Sportster", "Cruiser")
print(car.info())
print(moto.info())