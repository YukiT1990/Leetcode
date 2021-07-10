# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 1:
            return True

        charDict = {}

        for i in range(0,len(s)):
            if s[i] not in charDict.keys(): # check s[i] already exists in keys
                if t[i] not in charDict.values(): # check t[i] already exists in values
                    charDict[s[i]] = t[i]
                else: # different pair already exists
                    return False
            else: # different pair appears
                if charDict[s[i]] != t[i]:
                    return False
        return True
