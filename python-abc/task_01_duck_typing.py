#!/usr/bin/env python3
"""Module demonstrating duck typing with shapes using abstract base classes."""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class representing a geometric shape."""
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape.
        
        Returns:
            float: The area of the shape.
        """
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.
        
        Returns:
            float: The perimeter of the shape.
        """
        pass

class Circle(Shape):
    """Circle class implementing the Shape interface."""
    
    def __init__(self, radius):
        """Initialize a Circle with given radius.
        
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius
    
    def area(self):
        """Calculate the area of the circle.
        
        Returns:
            float: Area calculated as πr².
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate the circumference of the circle.
        
        Returns:
            float: Perimeter calculated as 2πr.
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Rectangle class implementing the Shape interface."""
    
    def __init__(self, width, height):
        """Initialize a Rectangle with given width and height.
        
        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate the area of the rectangle.
        
        Returns:
            float: Area calculated as width × height.
        """
        return self.width * self.height
    
    def perimeter(self):
        """Calculate the perimeter of the rectangle.
        
        Returns:
            float: Perimeter calculated as 2(width + height).
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing.
    
    Args:
        shape: An object that implements area() and perimeter() methods.
        
    Note:
        This function uses duck typing - it doesn't check the type of the object,
        only that it has the required methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
