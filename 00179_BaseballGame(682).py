# 682. Baseball Game

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = [int(ops[0])]
        for i in range(1, len(ops)):
            if ops[i] == '+':
                record.append(record[-2] + record[-1])
            elif ops[i] == 'D':
                record.append(2 * record[-1])
            elif ops[i] == 'C':
                record.pop(-1)
            else:
                record.append(int(ops[i]))
                
        # print(record)
        return sum(record)