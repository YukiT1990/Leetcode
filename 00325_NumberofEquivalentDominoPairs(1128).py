# 1128. Number of Equivalent Domino Pairs

import collections

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 540 ms	24.4 MB
        # 284 ms	24.4 MB
        for i in range(len(dominoes)):
            dominoes[i] = sorted(dominoes[i])
        dominoes = sorted(dominoes, key=lambda x: x[1])
        dominoes = sorted(dominoes, key=lambda x: x[0])
        # print(dominoes)
        set_dominoes = []
        count = 1
        result = 0
        for d in dominoes:
            if d not in set_dominoes:
                if count != 1:
                    result += count * (count-1) // 2
                count = 1
                set_dominoes.append(d)
            else: 
                count += 1
        if count != 1:
            result += count * (count-1) // 2  
        # print(set_dominoes)
        return result
    
    
        # 324 ms	23.9 MB
        # Reference
        # https://leetcode.com/problems/number-of-equivalent-domino-pairs/discuss/348400/python3-dictionary-count
        # step 1: count the dominoes
        # d = {}
        # for domi in dominoes:
        #     p = tuple(sorted(domi))
        #     if p in d:
        #         d[p] += 1
        #     else:
        #         d[p] = 1
        # # step 2: caculate the pairs. for each pair, number of pairs = n*(n-1)//2
        # c = 0
        # for n in d.values():
        #     s = n*(n-1)//2
        #     c += s
        # return c