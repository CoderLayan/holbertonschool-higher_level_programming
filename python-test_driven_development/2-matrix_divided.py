#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number and returns a new matrix.
    
    Args:
        matrix: A list of lists, where each element is an integer or float.
        div: The divisor (integer or float).
    
    Returns:
        A new matrix with each element divided by `div`, rounded to 2 decimal places.
    
    Raises:
        TypeError: If `matrix` is not a list of lists of numbers or if `div` is not a number.
        ZeroDivisionError: If `div` is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(element / div, 2) for element in row] for row in matrix]
