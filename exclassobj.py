#class is bluprint of obj. it encapsulates data for obj and methods to manipulate the data.

class Car:
    # Constructor to initialize the object
    def __init__(self, make, model, year):
        self.make= make #instance variable
        self.model= model
        self.year= year

    def disply_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def start_car(self):
        print(f"This {self.model} car is starting")

    def stop_car(self):
        print(f"This {self.model} car is stoping")

