# 734. Sentence Similarity

# Reference
# https://leetcode.com/problems/sentence-similarity/discuss/359418/Simple-solution

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            if not ([w1, w2] in similarPairs or [w2, w1] in similarPairs):
                return False
        return True
