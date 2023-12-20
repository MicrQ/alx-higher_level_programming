#!/usr/bin/python3
"""Node: to create new node"""


class Node:
    """Defines a new Node"""
    def __init__(self, data, next_node=None):
        """Initializer
        Args:
            data(int): data for the node
            next_node(Node): the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """data setter"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """setter of next_node"""
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""A singly linked list class"""


class SinglyLinkedList:
    """defines a node"""
    def __init__(self):
        """"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new node"""
        new = Node(value)
        ptr = self.__head
        hold = None

        if self.__head is None:
            new.next_node = None
            self.__head = new

        elif value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
        else:
            while (ptr.next_node is not None and
                    ptr.next_node.data < value):
                ptr = ptr.next_node
            new.next_node = ptr.next_node
            ptr.next_node = new

    def __str__(self):
        """str"""
        sData = []
        hold = self.__head

        while hold:
            sData.append(str(hold.data))
            hold = hold.next_node
        return ('\n'.join(sData))
