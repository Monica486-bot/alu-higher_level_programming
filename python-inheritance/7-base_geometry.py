#!/usr/bin/python3
"""defines class Rectangle that inherits from BaseGeometry"""

BaseGeometry = _import_('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class for rectangle that inherits from BaseGeometry
    with print() and str() ability"""
    def _init_(self, width, height):
        """initializes Rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def _str_(self):
        """string representation of Rectangle"""
        str_rep = "[Rectangle] " + str(self._width) + "/" + str(self._height)
        return str_rep

    def area(self):
        """returns area of rectangle"""
        return (self._width * self._height)
