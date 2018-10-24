"""
Given A Singly linkedList node implement a function to remove that node

Note 1: The runtime should be a constant time
Note 2: it is guarantee that the given node will not be the tail of the list

Runtme O(1)
"""

def remove_node(node):
    node.data = node.next.data
    node.next = node.next.next
