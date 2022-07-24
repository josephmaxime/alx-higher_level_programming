#!/usr/bin/python3


"""Node Module"""


class Node:
    """ class Node that defines a node of a singly linked list. """

    def __init__(self, data, next_node=None):

        """Initialize data and next_node of a current node.

        Args:

           data (int): value of a node.
           next_node (Node): a node or None.

        """

        if not isinstance(data, int):

            raise TypeError("data must be an integer")

        self.__data = data

        if not isinstance(next_node, Node) and next_node is not None:

            raise TypeError("next_node must be a Node object")

        self.__next_node = next_node

    @property
    def data(self):

        """Retrieve the data of node."""

        return self.__data

    @property
    def next_node(self):

        """Retreieve a next node of current node."""

        return self.__next_node

    @data.setter
    def data(self, value):

        """Set the new value of a data

        Args:

            value (int): the new value of data.

        """

        if not isinstance(value, int):

            raise TypeError("data must be an integer")

        self.__data = value

    @next_node.setter
    def next_node(self, value):

        """Set the new value of next node by curent node

        Args:

            value (Node): the new value of next node.

        """

        if not isinstance(value, Node) and value is not None:

            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list by head."""

    def __init__(self):
        """ Initialize a node """

        self.__head = None

    def __str__(self):
        """ String representation in singly linked list"""

        ch = ""
        ptr = self.__head

        while ptr is not None:
            ch += str(ptr.data)
            if ptr.next_node is not None:
                ch += "\n"
            ptr = ptr.next_node

        return ch

    def sorted_insert(self, value):
        """ that inserts a new Node into the correct
        sorted position in the list.

        Args:
            value (int): node to insert in sorted position.
        """

        new_node = Node(value, None)

        ptr = self.__head

        if ptr is None or ptr.data >= value:

            if ptr:

                new_node.next_node = ptr

            self.__head = new_node

            return

        while ptr.next_node is not None:

            if ptr.next_node.data >= value:

                break

            ptr = ptr.next_node

        new_node.next_node = ptr.next_node

        ptr.next_node = new_node
