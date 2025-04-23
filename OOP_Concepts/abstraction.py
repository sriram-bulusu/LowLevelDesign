# ABSTRACTION

"""
    Abstraction is a very similar concept to encapsulation. But there is a key difference. 

    Encapsulation refers to packaging everything into a class so that it cannot be accessed from outside the class.

    Abstraction refers to hiding the implementation details to reduce complexity for an average user. 

    For example, you can turn a car on by turning the key or pressing a button. You do not need to know the inner workings of
    the engine to start the car. 

    The following example will demonstrate the difference between encapsulation and abstraction.
"""

class Car():
    def __init__(self, make, model, year):
        self.make = make # Encapsulated attribute
        self.model = model # Encapsulated attribute
        self.year = year # Encapsulated attribute
        self.isStarted = False # Encapsulated attribute
        self.currentSpeed = 0 # Encapsulated attribute
    
    # Encapsulation: mathods operate on encapsulated attributes
    def start(self):
        if not self.isStarted:
            self.isStarted = True
            print("The car is now on")
        else:
            print("The car is already on")
    
    def accelerate(self, speed):
        if self.isStarted:
            self.currentSpeed += speed
            print(f"The car is accelrating. Current speed is {self.currentSpeed}")
        else:
            print("Car must be on")
    
    def stop(self):
        if self.isStarted:
            self.isStarted = False
            self.currentSpeed = 0
            print("Car is now off")
        else:
            print("Car is already off")

    # Abstraction: Method abstracts the concept of driving without exposing implementation details
    def drive(self, destination):
        self.start() # Abstraction: calling encapsulated method to start the car

        print(f"Driving to {destination}")

        self.accelerate(60) # Abstraction: calling encapsulated method to accelerate
        
        print(f"Arrived at {destination}")

        self.stop() # Abstraction: calling encapsulated method to stop the car



myCar = Car("MG", "Hector", "2021")
myCar.drive("Anusha Villa")
