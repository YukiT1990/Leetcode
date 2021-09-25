# 1022. Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(root: Optional[TreeNode], binary: str):
            nonlocal result
            if root:
                binary += str(root.val)
                if root.left:
                    dfs(root.left, binary)
                if root.right:
                    dfs(root.right, binary)
                if not root.left and not root.right:
                    # print(binary)
                    result += int(binary, 2)
            
        dfs(root, '')
        return result