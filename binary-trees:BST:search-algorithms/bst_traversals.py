"""
Pupose:
    Defines simple traversals for treenode (primitive) trees.
"""

import treenode as tn
import NQueue as Q


def pre_order(tnode):
    
    if tnode is None:
        return ""
    result = str(tnode.data)
    left_result = pre_order(tnode.left)
    right_result = pre_order(tnode.right)
    if left_result:
        result += " " + left_result
    if right_result:
        result += " " + right_result
    return result
    

def in_order(tnode):
    if tnode is None:
        return ""
    left_result = in_order(tnode.left)
    right_result = in_order(tnode.right)
    result = ""
    if left_result:
        result += left_result + " "
    result += str(tnode.data)
    if right_result:
        result += " " + right_result
    return result


def post_order(tnode):
    if tnode is None:
        return ""
    left_result = post_order(tnode.left)
    right_result = post_order(tnode.right)
    result = ""
    if left_result:
        result += left_result + " "
    if right_result:
        result += right_result + " "
    result += str(tnode.data)
    return result


def breadth_order(tnode):
    explore = Q.Queue()
    explore.enqueue(tnode)
    values = ""
    while explore.size() > 0:
        current = explore.dequeue()
        values += str(current.data) + " "
        if current.left is not None:
            explore.enqueue(current.left)
        if current.right is not None:
            explore.enqueue(current.right)
    return values


if __name__ == "__main__":
    tnode = tn.treenode(2,
                        tn.treenode(7, 
                                    tn.treenode(11), 
                                    tn.treenode(6)),
                        tn.treenode(5))

    print("Pre-order traversal:", end=" ")
    print(pre_order(tnode))

    print("In-order traversal:", end=" ")
    print(in_order(tnode))

    print("Post-order traversal:", end=" ")
    print(post_order(tnode))

    print("Breadth-order traversal:", end=" ")
    print(breadth_order(tnode))
