#!/usr/bin/python3
""" module rectangle defines class: Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ It initializes the object from class Rectangle
        args:
        width (int): the width of a rectangle (Private instance attribute)
        height (int): the height of a rectangle (Private instance attribute)
        x (int): the abscissa
        y (int): the ordinate
        id (int): the id of the object
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get/Set the value of/from width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Retrieve/set the value of/from height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Get/Set the value of/from x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Get/Set the value of/from y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ it returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """it prints in stdout the Rectangle instance with the character # """
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def display(self):
        """ it prints in stdout the Rectangle instance with the character #
        by taking care of x and y"""
        print ('\n' * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """it assigns an argument to each attribute:
        Args:
        *args (ints): attributes value:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        
        **kwargs (dict): assigns a key/value argument to attributes
        """
        if args and len(args) !=0:
            if len(args) == 1:
                self.id = args
            if len (args) == 2:
                (self.id, self.width) = args
            if len (args) == 3:
                (self.id, self.width, self.height) = args
            if len(args) == 4:
                (self.id, self.width, self.height, self.x) = args
            if len(args) >= 5:
                (self.id, self.width, self.height, self.x, self.y) = args[:5]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
