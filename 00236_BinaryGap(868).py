# 868. Binary Gap

class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        # print(binary)
        if len(binary) < 2:
            return 0
        max_count = 0
        count = 0
        found = False
        for i in range(len(binary)):
            if found == False and binary[i] == '1':
                found = True
            elif found == True and binary[i] == '0':
                count += 1
            elif found == True and binary[i] == '1':
                count += 1
                max_count = max(max_count, count)
                count = 0
        return max_count