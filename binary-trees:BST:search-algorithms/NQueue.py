"""
Purpose:
    Implements the Queue ADT. A queue (also called a FIFO queue) is a compound data structure in which the data values are ordered according to the 
    FIFO (first-in first-out) protocol. This implementation uses the linked node structure.
"""

import node as N


class Queue(object):
    def __init__(self):
        """
        Purpose:
            Initializes a new instance of the Queue class as an empty queue using a linked node structure.
        Pre-conditions:
            None (no parameters are needed to create an empty queue).
        Post-conditions:
            A new empty queue is created with initial size set to 0 and both front and back pointers set to None.
        Return:
            None (Constructor does not return a value).
        """
        self.__size = 0
        self.__front = None
        self.__back = None

    def size(self):
        """
        Purpose:
            Returns the current number of elements in the queue.
        Pre-conditions:
            None (simply accesses the current state).
        Post-conditions:
            None (the queue remains unchanged).
        Return:
            The number of elements in the queue as an integer.
        """
        return self.__size

    def is_empty(self):
        """
        Purpose:
            Checks if the queue is empty.
        Pre-conditions:
            None (simply assesses the queue's size).
        Post-conditions:
            None (the queue remains unchanged).
        Return:
            True if the queue is empty, otherwise False.
        """
        return self.__size == 0

    def enqueue(self, value):
        """
        Purpose:
            Adds a new element to the back of the queue.
        Pre-conditions:
            'value': The data value to be added to the queue.
        Post-conditions:
            The queue's size increases by one. The new element is placed at the back of the queue.
        Return:
            None (The method is used for adding an element to the queue).
        """
        new_node = N.node(value)
        if self.is_empty():
            self.__front = new_node
            self.__back = new_node
        else:
            self.__back.set_next(new_node)
            self.__back = new_node
        self.__size += 1
    
    def dequeue(self):
        """
        Purpose:
            Removes and returns the element at the front of the queue.
        Pre-conditions:
            The queue should not be empty (an assertion checks for this).
        Post-conditions:
            The queue's size decreases by one. The element previously at the front is removed.
        Return:
            The data value of the element that was removed from the front of the queue.
        """
        assert not self.is_empty(), "Dequeued an empty queue"
        result = self.__front.get_data()
        self.__front = self.__front.get_next()
        self.__size -= 1
        if self.__size == 0:
            self.__back = None
        return result

    def peek(self):
        """
        Purpose:
            Retrieves, but does not remove, the element at the front of the queue.
        Pre-conditions:
            The queue should not be empty (an assertion checks for this).
        Post-conditions:
            None (the queue remains unchanged).
        Return:
            The data value of the element at the front of the queue.
        """
        assert not self.is_empty(), "Peeked into an empty queue"
        first_node = self.__front
        result = first_node.get_data()
        return result
