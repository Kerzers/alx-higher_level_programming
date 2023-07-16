#!/usr/bin/python3
""" module rectangle defines class: Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """It initializes the object from class Square
        args:
        size (int): the size of a square
        x (int): the abscissa
        y (int): the ordinate
        id (int): the id of the object from class square

        Raises:
        [TypeError] size must be an integer
        [ValueError] size must be > 0
        [TypeError] x and y must be an integer
        [ValueError] x and y must be >= 0
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of a square instance"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """it returns [Square] (<id>) <x>/<y> - <size>"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """it assigns an argument to each attribute:
        Args:
        *args (ints): attributes value:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute

        **kwargs (dict): assigns a key/value argument to attributes
        """
        if args and len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                (self.id, self.size) = args
            if len(args) == 3:
                (self.id, self.size, self.x) = args
            if len(args) >= 4:
                (self.id, self.size, self.x, self.y) = args[:4]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ it returns the dictionary representation of a Square.
        This dictionary must contain:
        id, size, x, y
        """
        square_dict = {"id": self.id, "size": self.width,
                       "x": self.x, "y": self.y}
        return square_dict
