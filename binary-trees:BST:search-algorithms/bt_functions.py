"""
Purpose:
    Defines simple functions for treenode (primitive) trees.
"""

import treenode as tn


def is_leaf(tnode):
    return tnode is not None and tnode.left is None and tnode.right is None


def height(tnode):
    if tnode is None:
        return 0
    else:
        left_height = height(tnode.left)
        right_height = height(tnode.right)
    return 1 + max(left_height, right_height)


def member(tnode, value):
    if tnode is None:
        return None
    elif tnode.data == value:
        return True
    else:
        return member(tnode.left, value) or member(tnode.right, value)


def count(tnode):
    if tnode is None:
        return 0
    else:
        return 1 + count(tnode.left) + count(tnode.right)


if __name__ == "__main__":
    tnode = tn.treenode(2,
                        tn.treenode(7, 
                                    tn.treenode(11), 
                                    tn.treenode(6)),
                        tn.treenode(5))
    
    print(is_leaf(tnode))
    print(height(tnode))
    print(member(tnode, 7))
    print(count(tnode))
