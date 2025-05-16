#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: List of lists of integers/floats
        div: Number to divide by (integer/float)

    Returns:
        New matrix with divided elements rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                  or if rows have different sizes,
                  or if div is not a number
        ZeroDivisionError: If div is zero
    """
    # Validate matrix is a list of lists
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Validate all elements are numbers
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    # Validate all rows have same size
    row_size = len(matrix[0]) if matrix else 0
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    return [[round(x / div, 2) for x in row] for row in matrix]
