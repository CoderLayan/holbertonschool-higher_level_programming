"""Module containing improved BaseGeometry class with area method."""


class BaseGeometry:
    """Base geometry class with area method."""

    def area(self):
        """Calculate the area (not implemented).

        Raises:
            Exception: Always raises with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")
