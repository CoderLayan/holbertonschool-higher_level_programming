#!/usr/bin/python3
"""Defines a matrix division function."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor (number, integer or float).

    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If rows of matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists of numbers
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element by div and round to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
