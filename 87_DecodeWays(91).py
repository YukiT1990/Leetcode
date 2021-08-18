# 91. Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        validCodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                       '11', '12', '13', '14', '15', '16', '17', '18',
                       '19', '20', '21', '22', '23', '24', '25', '26']
        
        if len(s) == 0 or s[0] == '0':
            return 0
        
        results = [1, 1] + [0 for _ in range(len(s) - 1)]
        
        for i, char in enumerate(s[1:], 1): # start index from 1
            index = i + 1
            # if s[i] == '0' (special handling for '0')
            if char == '0':
                # either '10' or '20'
                if s[i - 1:i + 1] in validCodes:
                    results[index] = results[index - 2]
                else:
                    return 0
            # if s[i - 1:i + 1] == '10' ~ '26' except for '10' and '20'
            elif s[i - 1:i + 1] in validCodes:
                results[index] = results[index - 1] + results[index - 2]
            # if s[i] == '1' ~ '9'
            else:
                results[index] = results[index - 1]
                
        return results[-1]
        