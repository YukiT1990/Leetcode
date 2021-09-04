# 589. N-ary Tree Preorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        values = []
        def dfs(root: 'Node'):
            nonlocal values
            if root:
                values.append(root.val)
                if root.children != []:
                    for child in root.children:
                        dfs(child)
                        
        dfs(root)
            
        return values