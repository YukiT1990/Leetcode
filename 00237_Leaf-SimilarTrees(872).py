# 872. Leaf-Similar Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = []
        leaves2 = []
        def dfs(root: Optional[TreeNode], array):
            if root:
                if root.left:
                    dfs(root.left, array)
                if root.right:
                    dfs(root.right, array)
                if not root.left and not root.right:
                    array.append(root.val)
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        if leaves1 != leaves2:
            return False
        else:
            return True