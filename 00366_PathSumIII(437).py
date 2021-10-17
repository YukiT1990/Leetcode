# 437. Path Sum III

# Reference
# https://leetcode.com/problems/path-sum-iii/discuss/581442/Python-DFS-Recursive-Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cnt = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, start, s):
            if not root:
                return 
            s -= root.val
            if s == 0:
                self.cnt += 1
            dfs(root.left, False, s)
            dfs(root.right, False, s)
            if start:
                dfs(root.left, True, targetSum)
                dfs(root.right, True, targetSum)
                
        dfs(root, True, targetSum)
        return self.cnt