# 282. Expression Add Operators

# Reference
# https://leetcode.com/problems/expression-add-operators/discuss/1031229/Python-Simple-heavily-commented-and-accepted-Recursive-Solution

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        exprs = []
        
        def recurse(idx, value, delta, exp):
            # base case here
            if idx == len(num):
                if value == target:
                    exprs.append("".join(exp))
            
            # the loop will create the current operand and recursively call
            # the next set of actions to be executed
            for i in range(idx, len(num)):
                if num[idx] == '0' and i > idx:
                    return
                
                curr = int(num[idx:i+1])
                curr_str = num[idx:i+1]
                
                if idx == 0:
                    recurse(i+1, curr, curr, exp + [curr_str])
                else:
                    recurse(i+1, value+curr, curr, exp + ['+', curr_str])
                    recurse(i+1, value-curr, -curr, exp + ['-', curr_str])
                    recurse(i+1, (value-delta)+curr*delta, curr*delta, exp + ['*', curr_str])
                            
        recurse(0, 0, 0, [])
        return exprs
        