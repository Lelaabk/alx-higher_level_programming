#!/usr/bin/python3
""" This module defines the Square class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class, inherits from Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The unique identifier for the instance.

        Attributes:
            id (int): The unique identifier for the instance.
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.

        Calls the constructor of the Rectangle class,
        using `id`, `x`, `y`, and `size`.
        The width and height are both assigned the value of `size`.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for the size attribute. """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for the size attribute. """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assign attributes based on arguments or key-value arguments. """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Return a dictionary representation of the Square instance. """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y}

    def __str__(self):
        """Return a string representation of the Square instance. """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
