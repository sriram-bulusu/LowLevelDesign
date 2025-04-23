# INHERITANCE

"""
    Inheritance means a child(sub) class can inherit the attributes and methods of a parent(super) class.

    The subclass can add methods and attributes of its own and can also modify the existing superclass methods in it's own way
"""

class Vehicle:
    def __init__(self, color):
        self.color = color
    
    def honk(self):
        print("HONK HONK!!!!!!")

class Car(Vehicle):
    def __init__(self, color, speed):
        super().__init__(color)
        self.speed = speed
    
    def accelerate(self):
        self.speed += 10
        print("Vroom vroooooom!!")

myCar = Car("red", 20)
myCar.accelerate()
myCar.honk()
    
"""
    I created an object of Car which is a child of the Vehicle class and so it inherits the honk method.
    
    Also, when I set the color to red, in the init method of the Car class, it is instantiating the Vehicle class with the
    color red.
"""
