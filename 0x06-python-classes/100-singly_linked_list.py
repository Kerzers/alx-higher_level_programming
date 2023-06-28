#!/usr/bin/python3
"""The module defines the class node"""


class Node:
    """ Class that defines a node of a singly linked list by:
    Attributes:
        data (int): data
        next_node (Node): object to the next node
    """
    def __init__(self, data, next_node=None):
        """ Initialize the class Node by:

        Args:
        data (int): data
        next_node (Node): object to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieve the data from node object"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieve the value of next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Class that defines a singly linked list by:
    Attributes:
        head (Node): head of a singly linked list
    """
    def __init__(self):
        """Initilize the class SinglyLinkedList"""
        self.__head = None

    def __str__(self):
        """ Prints the entire list in stdout, one node per line"""
        result = ""
        current = self.__head
        if current is not None:
            while current.next_node is not None:
                result += str(current.data) + '\n'
                current = current.next_node
            result += str(current.data)

        return result

    def sorted_insert(self, value):
        """method that inserts a new Node into the correct sorted position\
                in the list (increasing order)

        Args:
        value (Node): new node to insert in a Single linked list
        """
        new_node = Node(value)
        new_node.next_node = None

        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node):
                if (current.next_node).data > new_node.data:
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    break

                current = current.next_node
            current.next_node = new_node
