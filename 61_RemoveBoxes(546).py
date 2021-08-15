# 546. Remove Boxes
# too difficult
# Reference
# https://leetcode.com/problems/remove-boxes/discuss/1402468/Python-5-lines-dp-O(n4)-solution-explained-in-details

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @lru_cache(None)
        # Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments.
        # If maxsize is set to None, the LRU feature is disabled and the cache can grow without bound.
        # Reference(https://docs.python.org/3/library/functools.html)
        def dp(i, j, k):
            if i > j:
                return 0
            index = [m for m in range(i + 1, j + 1) if boxes[m] == boxes[i]]
            ans = (k + 1) ** 2 + dp(i + 1, j, 0)
            return max([ans] + [dp(i + 1, m - 1, 0) + dp(m, j, k + 1) for m in index])

        return dp(0, len(boxes) - 1, 0)
