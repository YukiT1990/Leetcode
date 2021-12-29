# 116. Populating Next Right Pointers in Each Node

# Reference
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/934979/easy-BFS-Python-solution

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        q = collections.deque()

        q.append(root)

        while q:
            for i in range(1, len(q)):
                q[i-1].next = q[i]
            q[-1].next = None
            newLevel = deque()
            for node in q:
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)

            q = newLevel
        return root
