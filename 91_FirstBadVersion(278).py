# 278. First Bad Version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        cur_pos = n
        if n > 3:
            length = n // 2
            cur_pos = n // 2
            
            while length > 0:   
                if isBadVersion(cur_pos):
                    if isBadVersion(cur_pos -1) == False:
                        return cur_pos
                    cur_pos -= length
                else:
                    cur_pos += length
                length //= 2
            
        # current is bad
        if isBadVersion(cur_pos):
            found_good = False
            while cur_pos > 0:
                cur_pos -= 1
                if isBadVersion(cur_pos) == False:
                    found_good = True
                    return cur_pos + 1 
                if found_good == False and cur_pos == 1:
                        return 1
        # current is good
        else:
            while cur_pos <= n:
                cur_pos += 1
                if isBadVersion(cur_pos):
                    return cur_pos
            
        # Reference
        # https://leetcode.com/problems/first-bad-version/discuss/708387/Yet-another-Python-solution
        # l,r=0,n
        # while l<r:
        #     mid = (l+r)//2
        #     if isBadVersion(mid):
        #         r=mid
        #     else:
        #         l=mid+1
        # return l  