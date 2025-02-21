"""
Purpose: 
    Defines a node ADT. A node is a simple container with two pieces of information.
Pre-conditions:
    'data': the contained information
    'next': a reference to another node
"""

class node(object):
    def __init__(self, data, next=None):
        """
        Purpose:
            Initializes a new instance of the node class with specified data and a reference to the next node.
        Pre-conditions:
            None explicitly required; method is used to create a new node.
        Post-conditions:
            A new node object is created with the specified 'data' and 'next' values.
        Return:
            None (Constructor does not return a value).
        """
        self.__data = data
        self.__next = next

    def get_data(self):
        """
        Purpose:
            Retrieves the data stored in this node.
        Pre-conditions:
            None; this method does not modify the node.
        Post-conditions:
            None; the node remains unchanged.
        Return:
            Returns the data contained in this node.
        """
        return self.__data

    def get_next(self):
        """
        Purpose:
            Retrieves the reference to the next node linked by this node.
        Pre-conditions:
            None; this method does not modify the node.
        Post-conditions:
            None; the node remains unchanged.
        Return:
            Returns the reference to the next node, or None if no next node exists.
        """
        return self.__next

    def set_data(self, value):
        """
        Purpose:
            Sets or updates the data stored in this node.
        Pre-conditions:
            'value': The new data to be stored in the node.
        Post-conditions:
            The data of this node is updated to the new value.
        Return:
            None (The method is used for setting a value).
        """
        self.__data = value

    def set_next(self, value):
        """
        Purpose:
            Sets or updates the reference to the next node.
        Pre-conditions:
            'value': Can be either another node or None. It is the new reference to be set as the next node.
        Post-conditions:
            The reference to the next node of this node is updated to the new value.
        Return:
            None (The method is used for setting a value).
        """
        self.__next = value
