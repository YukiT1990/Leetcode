# 559. Maximum Depth of N-ary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        max_depth = 0
        def helper(root: 'Node', depth: int):
            nonlocal max_depth
            if root:
                if root.children != []:
                    for child in root.children:
                        helper(child, depth+1)
                else:
                    # print(depth)
                    max_depth = max(max_depth, depth)
            elif not root:
                # print(depth)
                max_depth = max(max_depth, depth)
            
        if root:
            helper(root, 1)
            return max_depth
        else:
            return 0