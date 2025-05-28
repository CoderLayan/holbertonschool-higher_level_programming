#!/usr/bin/python3
MyList = __import__('my_list_1_6').MyList

# Test with populated list
ml = MyList()
ml.append(3)
ml.append(1)
ml.append(2)
print("Original:", ml)
ml.print_sorted()
print("Original preserved:", ml)

# Test with empty list
empty = MyList()
print("Empty list:", empty)
empty.print_sorted()
print("Still empty:", empty)
