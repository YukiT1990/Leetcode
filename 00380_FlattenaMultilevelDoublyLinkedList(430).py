# 430. Flatten a Multilevel Doubly Linked List

# Reference
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/948231/Elegant-Iterative-Solution

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def traverseChild(self, head):
        tail = head
        while tail and tail.next:
            tail = tail.next
        return tail

    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        while curr:
            if curr.child:
                tail = self.traverseChild(curr.child)
                tail.next = curr.next
                if tail.next:
                    tail.next.prev = tail
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            curr = curr.next
        return head
