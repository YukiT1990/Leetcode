# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def postorder(root, nodeVals: []):
    if root:
        postorder(root.left, nodeVals)
        postorder(root.right, nodeVals)
        nodeVals.append(root.val)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        nodeVals = []

        postorder(root, nodeVals)

        return nodeVals
