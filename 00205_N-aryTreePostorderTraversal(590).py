# 590. N-ary Tree Postorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        values = []
        def dfs(root: 'Node'):
            nonlocal values
            if root:
                if root.children != []:
                    for child in root.children:
                        dfs(child)
                values.append(root.val)
                        
        dfs(root)
            
        return values