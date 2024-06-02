from exclassobj import Car

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make,model,year) #initialize attribute from the parent class
        self.battery_size=battery_size #new attribute specific to electric car

    def disply_batt_info(self):
        print(f"The {self.model} has a {self.battery_size}-kWh battery.")


electric_car1 = ElectricCar("tesla","model s",2024, 1000)

electric_car1.disply_info()
electric_car1.disply_batt_info()
electric_car1.start_car()
electric_car1.stop_car()