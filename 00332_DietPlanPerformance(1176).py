# 1176. Diet Plan Performance

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        output = 0
        temp_sum = sum(calories[:k])
        for i in range(len(calories)-k+1):
            if temp_sum < lower:
                output -= 1
            elif temp_sum > upper:
                output += 1
            if i != len(calories)-k:
                temp_sum = temp_sum - calories[i] + calories[i+k]
        return output