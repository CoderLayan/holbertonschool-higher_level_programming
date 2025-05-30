#!/usr/bin/env python3
"""Module for Animal abstract class and its implementations."""
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class representing an animal."""
    
    @abstractmethod
    def sound(self):
        """Abstract method that should return the sound the animal makes.
        
        Returns:
            str: The sound of the animal.
        """
        pass

class Dog(Animal):
    """Dog class that inherits from Animal."""
    
    def sound(self):
        """Returns the sound a dog makes.
        
        Returns:
            str: The sound 'Bark'.
        """
        return "Bark"

class Cat(Animal):
    """Cat class that inherits from Animal."""
    
    def sound(self):
        """Returns the sound a cat makes.
        
        Returns:
            str: The sound 'Meow'.
        """
        return "Meow"
