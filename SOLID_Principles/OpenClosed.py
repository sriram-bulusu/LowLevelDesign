"""
    Below is an example of how the Open Closed principle works
"""

# How not to do it

class ShapeCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * (shape.radius**2)
    
    def calculate_perimeter(self, shape):
        if shape.type == "rectangle":
            return 2 * (shape.width + shape.height)
        elif shape.type == "circle":
            return 2 * 3.14 * shape.radius
        
"""
    The glaring issue here is that if we want to add another shape, like triangle, we have to modify the calculation methods.

    This violates the Open Closed principle
"""

# Correct way to do it

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * (self.radius**2)
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

"""
    By doing this, if we want to scale it to another shape, we can just create another class for that shape as a child of the
    Shape class and write it's own methods for area and perimeter.
"""