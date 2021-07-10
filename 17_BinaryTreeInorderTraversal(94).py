# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorder(root, result: []) -> []:
        if root:
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)
        return result
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        inorder(root, result)
        return result
