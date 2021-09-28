# 1160. Find Words That Can Be Formed by Characters

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # 176 ms	14.9 MB
        # chars = list(chars.strip())
        # result = 0
        # for word in words:
        #     copy_chars = chars[:]
        #     i = 0
        #     while i < len(word):
        #         if word[i] not in copy_chars:
        #             break
        #         else:
        #             copy_chars.remove(word[i])
        #             if i == len(word) - 1:
        #                 result += len(word)
        #         i += 1
        # return result
    
    

        # 168 ms	14.7 MB
        # Reference
        # https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/discuss/806134/Python-or-Using-Dictionaries-or-Please-Suggest-improvements
        from collections import Counter
        d = Counter(chars)
        ans=0
        for word in words:
            flag=0
            newD = Counter(word)
            for key in newD.keys():
                try:
                    if d[key]>=newD[key]:
                        flag=1
                    else:
                        flag=0
                        break
                except:
                    pass
            if flag:
                ans+=len(word)
            
            
        return(ans)