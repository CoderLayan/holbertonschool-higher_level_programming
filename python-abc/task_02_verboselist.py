#!/usr/bin/env python3
"""VerboseList implementation that notifies on modifications."""

class VerboseList(list):
    """A list that prints notifications for modifications."""
    
    def append(self, item):
        """Add an item to the end of the list with notification.
        
        Args:
            item: The item to be added.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        """Extend the list with items from iterable with notification.
        
        Args:
            iterable: An iterable of items to add.
        """
        length_before = len(self)
        super().extend(iterable)
        num_added = len(self) - length_before
        print(f"Extended the list with [{num_added}] items.")
    
    def remove(self, item):
        """Remove first occurrence of item with notification.
        
        Args:
            item: The item to be removed.
        
        Raises:
            ValueError: If item not found.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """Remove and return item at index with notification.
        
        Args:
            index: Index of item to pop (default last).
        
        Returns:
            The popped item.
        """
        item = self[index]  # Get item before popping for message
        result = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return result
