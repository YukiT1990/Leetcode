# 129. Sum Root to Leaf Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        values = []

        def dfs(root: Optional[TreeNode], num: str):
            nonlocal values
            if root:
                num += str(root.val)
                if root.left:
                    dfs(root.left, num)
                if root.right:
                    dfs(root.right, num)
                if not root.left and not root.right:
                    values.append(int(num))

        dfs(root, "")
        return sum(values)
