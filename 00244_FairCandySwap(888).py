# 888. Fair Candy Swap

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        AminusB = sum(aliceSizes) - sum(bobSizes)
                
        for i in aliceSizes:
            if i - AminusB // 2 in bobSizes:
                return [i, i - AminusB // 2]