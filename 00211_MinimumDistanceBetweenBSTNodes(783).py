# 783. Minimum Distance Between BST Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []
        def dfs(root: Optional[TreeNode]):
            nonlocal values
            if root:
                values.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
                
        dfs(root)
        values.sort()
        min_diff = 10 ** 5
        for i in range(len(values) - 1):
            min_diff = min(min_diff, values[i+1] - values[i])
            
        return min_diff