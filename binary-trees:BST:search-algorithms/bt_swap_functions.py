"""
Purpose:
    Treenode swap functions.
"""

import treenode as tn


def swap_left_right(tnode):
    """
    Purpose
        Swap the left and right of a given treenode
    Pre-conditions:
        tnode: A Treenode
    Post-condition:
        The Treenode passed in will have left and right swapped
    Return:
        None
    """
    if tnode is not None:
        temp = tnode.left
        tnode.left = tnode.right
        tnode.right = temp


def mirror_tree(tnode):
    """
    Purpose
        Swap the left and right of a given treenode. This is done for all child nodes
    Pre-conditions:
        tnode: A Treenode
    Post-condition:
        The Treenode passed in will have left and right swapped throughout the whole tree
    Return:
        None
    """
    if tnode is not None:
        temp = tnode.left
        tnode.left = tnode.right
        tnode.right = temp
        
        mirror_tree(tnode.left)
        mirror_tree(tnode.right)


def print_inorder(tnode):
    if tnode is not None:
        print_inorder(tnode.left)
        print(tnode.data, end=' ')
        print_inorder(tnode.right)


if __name__ == "__main__":
    tnode = tn.treenode(2,
                        tn.treenode(7, 
                                    tn.treenode(11), 
                                    tn.treenode(6)),
                        tn.treenode(5))
    
    print('Original Tree Inorder')
    print_inorder(tnode)
    print()


    swap_left_right(tnode)
    print('Mirrored Tree Inorder')
    print_inorder(tnode)
    print()
