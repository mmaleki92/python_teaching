class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def drive(self):
        print(f"The {self.make} {self.model} is driving.")
        
my_car = Car("Tesla", "Model S", 2022)
print(my_car.make)
print(my_car.year)
my_car.drive()