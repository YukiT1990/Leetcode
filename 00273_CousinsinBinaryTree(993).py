# 993. Cousins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # 32 ms	14.4 MB
        depth_x = -1
        depth_y = -2
        parent_x = -1
        parent_y = -2
        def dfs(root: Optional[TreeNode], x: int, y: int, depth: int, parent: int):
            nonlocal depth_x
            nonlocal depth_y
            nonlocal parent_x
            nonlocal parent_y
            if root:
                if root.val == x:
                    depth_x = depth
                    parent_x = parent
                if root.val == y:
                    depth_y = depth
                    parent_y = parent
                if root.left:
                    dfs(root.left, x, y, depth+1, root.val)
                if root.right:
                    dfs(root.right, x, y, depth+1, root.val)
                    
        dfs(root, x, y, 0, -1)
        # print(depth_x)
        # print(depth_y)
        return depth_x == depth_y and parent_x != parent_y
    
    
      # 28 ms	14.3 MB
      # Reference
      # https://leetcode.com/problems/cousins-in-binary-tree/discuss/741717/Python-beats-98-(easy-to-understand)-with-explanation
      #   def dept(node, d, par):
      #       if not node: return 
			# # if we find node with value x, then keep its depth and parent in a and aparent variables
      #       if node.val == x:
      #           self.a = d
      #           self.aparent= par
			# # if we find node with value y, then keep its depth and parent in b and bparent variables
      #       elif node.val == y:
      #           self.b = d
      #           self.bparent= par
      #       dept(node.left, d+1, node)
      #       dept(node.right, d+1, node)
      #   dept(root, 0, None)
      #   # return True if a and b are equal and their parents are not same
      #   return self.a == self.b and self.aparent != self.bparent