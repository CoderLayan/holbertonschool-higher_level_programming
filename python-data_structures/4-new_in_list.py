#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """we checked then created copy, return copy if not we change"""
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
