# 506. Relative Ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if len(score) == 1:
            return ["Gold Medal"]
        elif len(score) == 2:
            if score[0] > score[1]:
                return ["Gold Medal", "Silver Medal"]
            else:
                return ["Silver Medal" ,"Gold Medal"]
        sorted_score = sorted(score, reverse=True)
        result = []
        for num in score:
            if num == sorted_score[0]:
                result.append("Gold Medal")
            elif num == sorted_score[1]:
                result.append("Silver Medal")
            elif num == sorted_score[2]:
                result.append("Bronze Medal")
            else:
                result.append(str(sorted_score.index(num) + 1))
        return result