class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def fuel_type(self):
        return "Fuel"

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electricity"

car = ElectricCar("Tesla")

print("Brand:", car.brand)
print("Fuel Type:", car.fuel_type())