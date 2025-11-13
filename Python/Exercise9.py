# OOP – Class and Inheritance
class Vehicle:
    def __init__(self, makes, model):
        self.makes = makes
        self.model = model

class Car(Vehicle):
    def __init__(self, makes, model, num_doors):
        super().__init__(makes, model)
        self.num_doors = num_doors

    def display(self):
        print("Makes:", self.makes)
        print("Model:", self.model)
        print("Number of doors:", self.num_doors)

c = Car("Toyota", "Innova", 4)
c.display()