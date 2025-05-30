#!/usr/bin/env python3
"""Module demonstrating mixins with Dragon class."""

class SwimMixin:
    """Mixin class providing swimming capability."""
    
    def swim(self):
        """Print swimming message."""
        print("The creature swims!")

class FlyMixin:
    """Mixin class providing flying capability."""
    
    def fly(self):
        """Print flying message."""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining swimming and flying abilities."""
    
    def roar(self):
        """Print dragon's roar."""
        print("The dragon roars!")
