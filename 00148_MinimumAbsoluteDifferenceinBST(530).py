# 530. Minimum Absolute Difference in BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Inf = float('inf')
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        def collect_values(root: Optional[TreeNode]):
            nonlocal values
            if root:
                values.append(root.val)
            if root.left:
                collect_values(root.left)
            if root.right:
                collect_values(root.right)
            
        collect_values(root)
        
        min_dif = 10 ** 5
        values.sort()
        for i in range(len(values) - 1):
            min_dif = min(min_dif, values[i + 1] - values[i])
        return min_dif
    
        # Different answer
        # https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/758018/Python-DFS-or-100-Speed-or-Clean-Code
        # self.best = Inf = self.Inf
        # def dfs(n,a,b):
        #     if n:
        #         x = n.val
        #         self.best = min( self.best, x-a, b-x )
        #         dfs(n.left ,a,x)
        #         dfs(n.right,x,b)
        # dfs(root,-Inf,Inf)
        # return self.best
        