# 884. Uncommon Words from Two Sentences

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_list = list(s1.split(' '))
        s2_list = list(s2.split(' '))
        s1_set = set(list(s1.split(' ')))
        s2_set = set(list(s2.split(' ')))
        
        for word in s1_list:
            if s1_list.count(word) > 1:
                s1_set.discard(word)
                s2_set.discard(word)
                
        for word in s2_list:
            if s2_list.count(word) > 1:
                s1_set.discard(word)
                s2_set.discard(word)
        
        return s1_set ^ s2_set