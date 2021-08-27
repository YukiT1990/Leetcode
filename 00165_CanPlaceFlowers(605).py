# 605. Can Place Flowers

# Reference
# https://leetcode.com/problems/can-place-flowers/discuss/1048610/Python-Simple-solution-using-counting

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                count += 1
                flowerbed[i] = 1
                
        return count >= n
                
        