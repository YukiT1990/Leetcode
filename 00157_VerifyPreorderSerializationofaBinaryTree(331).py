# 331. Verify Preorder Serialization of a Binary Tree

# Reference
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/846494/Clear-Python-3-solution-faster-than-95-without-using-stack-comments-provided

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = deque(preorder.split(','))
        # number(s) of 'null'/'None' to take care of at any point in time, which is greater then the number of nodes by one
        count = 1
        while nodes:
            node = nodes.popleft()
            if node != '#':
                count += 1
            else:
                count -= 1
            if not count and nodes:
                return False
        if count:
            return False
        return True