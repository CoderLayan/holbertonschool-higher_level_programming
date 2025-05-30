#!/usr/bin/env python3
"""CountedIterator implementation that tracks iteration count."""

class CountedIterator:
    """Iterator wrapper that counts how many items have been fetched."""
    
    def __init__(self, iterable):
        """Initialize with an iterable and reset counter.
        
        Args:
            iterable: An iterable object to create iterator from.
        """
        self.iterator = iter(iterable)
        self.counter = 0
    
    def __next__(self):
        """Fetch next item and increment counter.
        
        Returns:
            The next item from the iterator.
            
        Raises:
            StopIteration: When no more items available.
        """
        item = next(self.iterator)  # May raise StopIteration
        self.counter += 1
        return item
    
    def get_count(self):
        """Return number of items fetched so far.
        
        Returns:
            int: The count of items iterated.
        """
        return self.counter
    
    def __iter__(self):
        """Return self to make iterator work in for-loops."""
        return self
