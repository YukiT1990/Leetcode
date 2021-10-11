# 543. Diameter of Binary Tree

# Reference
# https://leetcode.com/problems/diameter-of-binary-tree/discuss/1351854/Python-Iterative-solution-40-ms-faster-than-90.06-15.2-MB-less-than-99.95

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        hm = {}
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    lh = 0 if node.left is None else hm.pop(node.left)
                    rh = 0 if node.right is None else hm.pop(node.right)
                    ans = max(ans, lh + rh)
                    hm[node] = max(lh, rh) + 1
                else:
                    stack.append((node, True))
                    stack.append((node.left, False))
                    stack.append((node.right, False))
        return ans