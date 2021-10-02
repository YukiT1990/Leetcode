# 174. Dungeon Game

# Reference
# https://leetcode.com/problems/dungeon-game/discuss/404174/Easy-Python3-solution

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, columns = len(dungeon), len(dungeon[0])
        hp = [[0]*columns for i in range(rows)]
        
        
        # We will start at endpoint:
        hp[-1][-1] = max(1, 1-dungeon[-1][-1]) # in example we will need 6 HP to cover -5 loss
        
        # Completing the border lines. Excluding endpoint everywhere
        for i in range(rows-2, -1, -1):
            hp[i][-1] = max(1, hp[i+1][-1] - dungeon[i][-1])  
        for j in range(columns-2, -1, -1): 
            hp[-1][j] = max(1, hp[-1][j+1] - dungeon[-1][j])
        
        # print(hp) to see our HealthPoint table
        
		
        # Next we complete the remaining table
        for i in range(rows-2, -1, -1):
            for j in range(columns-2, -1, -1):                
                hp[i][j] = max(1, min(hp[i+1][j] - dungeon[i][j], hp[i][j+1] - dungeon[i][j]) )
        
        return hp[0][0]