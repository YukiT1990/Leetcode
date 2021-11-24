# 986. Interval List Intersections

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        i = 0
        j = 0
        result = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] < secondList[j][0]:
                if firstList[i][1] >= secondList[j][0]:
                    if firstList[i][1] < secondList[j][1]:
                        result.append([secondList[j][0], firstList[i][1]])
                        i += 1
                    else:
                        result.append([secondList[j][0], secondList[j][1]])
                        j += 1
                else:
                    i += 1

            else:
                if secondList[j][1] >= firstList[i][0]:
                    if secondList[j][1] < firstList[i][1]:
                        result.append([firstList[i][0], secondList[j][1]])
                        j += 1
                    else:
                        result.append([firstList[i][0], firstList[i][1]])
                        i += 1
                else:
                    j += 1

        return result
