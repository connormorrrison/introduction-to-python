"""
Purpose:
    Defines the treenode ADT. A treenode is a simple container with three pieces of information.
Pre-conditions:
    'data': the contained information.
    'left': a reference to another treenode or None.
    'right': a reference to another treenode or None.
"""

class treenode(object):
    def __init__(self, data, left=None, right=None):
        """
        Purpose:
            Initializes a new instance of the treenode class with specified data and optional references to left and right child nodes.
        Pre-conditions:
            'data': the contained information, can be of any data type.
            'left': a reference to another treenode or None, intended to represent the left child in a binary tree.
            'right': a reference to another treenode or None, intended to represent the right child in a binary tree.
        Post-conditions:
            A new treenode object is created with the specified 'data', 'left', and 'right' values. This node is ready to be used in a binary tree structure.
        Return:
            None (Constructor does not return a value, it is used to initialize the object).
        """
        self.data = data
        self.left = left
        self.right = right
