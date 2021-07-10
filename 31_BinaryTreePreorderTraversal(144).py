# 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorder(root, nodeVals: []):
    if root:
        nodeVals.append(root.val)
        preorder(root.left, nodeVals)
        preorder(root.right, nodeVals)

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        nodeVals = []

        preorder(root, nodeVals)

        return nodeVals
