# 293. Flip Game

# Reference
# https://leetcode.com/problems/flip-game/discuss/358954/python3-straight-forward-solution

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result = []
        
        for i in range(len(currentState) - 1):
            if currentState[i:i + 2] == '++':
                result.append(currentState[:i] + '--' + currentState[i + 2:])
            
        return result
        