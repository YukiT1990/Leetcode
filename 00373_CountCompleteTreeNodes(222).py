# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
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
        return len(values)
