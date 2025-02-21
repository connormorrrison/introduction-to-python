"""
Purpose:
    Defines functions for primitive Binary Search Tree data structure

    A Primitive Binary Tree is defined as follows:
    1. The value None is a primitive binary tree;
    None is an empty tree.
    2. If lt and rt are primitive binary trees, and d is any value
    treenode.create(d, lt, rt) is a primitive binary tree.

    A Primitive Binary Tree t satisfies the Binary Search Tree property
    if all of the following hold:
    1. The data value stored in t is greater than any data value in
    t's left subtree (if any)
    2. The data value stored in t is less than any data value in
    t's right subtree (if any)
    3. T's left subtree satisfies the BST property
    4. T's right subtree satisfies the BST property
"""

import treenode as tn


def member_prim(tnode, value):
    """
    Purpose:
        Check if value is stored in the binary search tree.
    Preconditions:
        :param tnode: a binary search tree
        :param value: a value
    Postconditions:
        none
    :return: True if value is in the tree
    """
    if tnode is None:
        return False
    
    elif tnode.data == value:
        return True
    
    elif value < tnode.data:
        return member_prim(tnode.left, value)
    
    else:
        return member_prim(tnode.right, value)


def insert_prim(tnode, value):
    """
    Insert a new value into the binary tree.
    Preconditions:
        :param tnode: a binary search tree
        :param value: a value
    Postconditions:
        If the value is not already in the tree, it is added
    Return
        :return: flag, tree
        Flag is True if insertion succeeded;
                tree contains the new value
        Flag is False if the value is already in the tree,
                tree unchanged
    """
    if tnode is None:
        return True, tn.treenode(value)
    elif tnode.data == value:
        return False, tnode
    elif value < tnode.data:
        flag, subtree = insert_prim(tnode.left, value)
        if flag:
            tnode.left = subtree
        return flag, tnode
    else:
        flag, subtree = insert_prim(tnode.right, value)
        if flag:
            tnode.right = subtree
        return flag, tnode


def delete_prim(tnode, value):
    """
    Delete a value from the binary tree.
    Preconditions:
        :param tnode: a binary search tree, created by create()
        :param value: a value
    Postconditions:
        If the value is in the tree, it is deleted.
        If the value is not there, there is no change to the tree.
    :return: True is the value was deleted, False otherwise
    """
    def delete_bst(tnode):
        if tnode is None:
            return False, tnode
        else:
            current_value = tnode.data
            if current_value == value:
                return reconnect(tnode)
            elif value < current_value:
                flag, subtree = delete_bst(tnode.left)
                if flag:
                    tnode.left = subtree
                return flag, tnode
            else:
                flag, subtree = delete_bst(tnode.right)
                if flag:
                    tnode.right = subtree
                return flag, tnode

    def reconnect(deleted_value):
        # The deleted node has no children
        if deleted_value.left is None and deleted_value.right is None:
            return True, None
        # The deleted node has one right child
        elif deleted_value.left == None:
            return True, deleted_value.right
        # The deleted node has one leff child
        elif deleted_value.right == None:
            return True, deleted_value.left
        # The deleted node has two children
        else:
            left = deleted_value.left
            right = deleted_value.right
            walker = left
            # Walk all the way to the right from left
            while walker.right != None:
                walker = walker.right
            walker.right = right
            return True, left

    flag, tree = delete_bst(tnode)
    return flag, tree


if __name__ == "__main__":
    tnode = tn.treenode(8, 
                        tn.treenode(5,
                                    tn.treenode(1),
                                    tn.treenode(6)), 
                        tn.treenode(10))
    
    print(member_prim(tnode, 5))
    print(insert_prim(tnode, 5))
    print(delete_prim(tnode, 5))
