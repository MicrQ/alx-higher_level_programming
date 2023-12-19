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
        data(data)
        next_node(next_node)


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
        if type(value) != Node and value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

"""A singly linked list class"""


class SinglyLinkedList:
    """defines a node"""
    def __init__(self):
        """"""
        pass

    def sorted_insert(self, value):
        """inserts a new node"""
        