# 700. Search in a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node: Optional[TreeNode] = None
        def dfs(root: Optional[TreeNode], val: int):
            nonlocal node
            if root:
                if root.val == val:
                    node = root
                    return
                if root.left:
                    dfs(root.left, val)
                if root.right:
                    dfs(root.right, val)
                             
        dfs(root, val)
        return node