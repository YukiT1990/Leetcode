# 637. Average of Levels in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
          # 73 ms	17.3 MB
        values = {}
        result = []
        def search_node(root: Optional[TreeNode], depth: int):
            nonlocal values
            if depth not in values.keys():
                values[depth] = [root.val]
            else:
                values[depth].append(root.val)
            if root.left:
                search_node(root.left, depth + 1)
            if root.right:
                search_node(root.right, depth + 1)
        
        search_node(root, 0)
        for i in range(len(values)):
            result.append(sum(values[i]) / len(values[i]))
            
        return result
    
    
        # 40 ms	16.8 MB
        # Reference
        # https://leetcode.com/problems/average-of-levels-in-binary-tree/discuss/1094550/Python3-solution-for-Average-of-Levels-in-Binary-Tree
        # q = []
        # curr = [root] #traverses one level at a time
        
        # while curr :
        #     q.append(curr)
        #     curr = []
        #     for node in q[-1] :
        #         # q of -1 means basically the most recently added level of the bt to the q
        #         if node.left:
        #             curr.append(node.left)
        #         if node.right:
        #             curr.append(node.right)
        # values = [[node.val for node in curr] for curr in q ]
        # print(values)  # [[3], [9, 20], [15, 7]]
        
        # return([sum(level)/len(level) for level in values])