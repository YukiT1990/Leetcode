# 633. Sum of Square Numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 364 ms	15.8 MB
        if c == 0:
            return True
        n = int(math.sqrt(c))
        
        squrelist = [0 for _ in range(n + 1)]
        
        for i in range(n + 1):
            squrelist[i] = i ** 2
            
        left = 0
        right = n
        
        while(left <= right):
            if squrelist[left] + squrelist[right] == c:
                return True
            elif squrelist[left] + squrelist[right] > c:
                right -= 1
            else:
                left += 1
        return False


        # Reference
        # https://leetcode.com/problems/sum-of-square-numbers/discuss/536537/Python-3-3-easy-solutions-(brief-explanation)

        # 548 ms	14.3 MB 
        # left = 0
        # right = int(math.sqrt(c))
        
        # while(left <= right):
        #     if left ** 2 + right ** 2 == c:
        #         return True
        #     elif left ** 2 + right ** 2 > c:
        #         right -= 1
        #     else:
        #         left += 1
        # return False


        # 368 ms	14.3 MB
        # def isSquare(n):
        #     return int(sqrt(n)) ** 2 == n
        
        # return any(isSquare(c-num**2) for num in range(int(sqrt(c))+1))


        # 348 ms	14 MB
        # if c == 0:
        #     return True
        
        # for i in range(1, int(math.sqrt(c) + 1)):
        #     j = c - i ** 2
        #     if int(math.sqrt(j)) ** 2 == j:
        #         return True
        # return False