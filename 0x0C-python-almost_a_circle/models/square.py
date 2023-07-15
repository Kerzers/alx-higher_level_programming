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
        Rectangle.__init__(self, size, size, x, y, id=None)

    def __str__(self):
        """it returns [Square] (<id>) <x>/<y> - <size>"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
