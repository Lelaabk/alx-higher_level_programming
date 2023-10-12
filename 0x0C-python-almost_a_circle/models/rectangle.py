#!/usr/bin/python3
""" This module defines the Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class, inherits from Base. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): The unique identifier for the instance.

        Attributes:
            id (int): The unique identifier for the instance.
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.

        Calls the constructor of the Base class, using `id`.
        Assigns the provided `width`, `height`, `x`, and `y`
        values to the corresponding attributes.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for the width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for the x attribute. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for the x attribute. """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for the y attribute. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the y attribute. """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculate and return the area of the rectangle. """
        return self.__width*self.__height

    def display(self):
        """ Display the Rectangle instance with '#' characters. """
        for i in range(self.__height):
            print("#" * self.__width)
