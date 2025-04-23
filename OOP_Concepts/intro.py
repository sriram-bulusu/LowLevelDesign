# design a class for a car

class Car:
    # the car will be initialized with these details while creating the Car object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_car(self):
        print(f"The {self.make} {self.model}'s engine is starting...")

    def check_year(self):
        print(f"This {self.make} {self.model} was manufactured in {self.year}.")


# creating an object of the the Car class by giving make, model, and year as attributes
myCar = Car("MG", "Hector", "2021")

# testing the methods of the Car class
myCar.start_car()
myCar.check_year()