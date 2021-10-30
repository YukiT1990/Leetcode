# 1044. Longest Duplicate Substring

# Reference
# https://leetcode.com/problems/longest-duplicate-substring/discuss/695144/Intuitive-Python3-Solution-O(nlogn)-Time-O(n)-Space

p = 2**63 - 1


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def rabin_karp(mid):
            cur_hash = 0
            for i in range(mid):
                cur_hash = (cur_hash * 26 + nums[i]) % p
            hashes = {cur_hash}
            pos = -1
            max_pow = pow(26, mid, p)
            for i in range(mid, len(s)):
                cur_hash = (26*cur_hash-nums[i-mid]*max_pow + nums[i]) % p
                if cur_hash in hashes:
                    pos = i + 1 - mid
                hashes.add(cur_hash)
            return pos

        low, high = 0, len(s)-1
        end = 0
        start = 0
        nums = [ord(c)-ord('a') for c in s]
        while low <= high:
            mid = (low+high) // 2
            pos = rabin_karp(mid)
            if pos == -1:  # no matching strings found
                high = mid - 1
            else:
                start = pos
                low = mid + 1
        return s[start:start+low-1]
