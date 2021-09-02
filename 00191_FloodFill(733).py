# 733. Flood Fill

# Reference
# https://leetcode.com/problems/flood-fill/discuss/626424/Python-sol-by-DFS-and-BFS-w-Comment

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        
        def helper(image: List[List[int]], src_color, r: int, c: int, newColor: int):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or (r,c) in visited or image[r][c] != src_color:
                return
            image[r][c] = newColor
            visited.add( (r,c) )
            helper(image, src_color, r-1, c, newColor)
            helper(image, src_color, r+1, c, newColor)
            helper(image, src_color, r, c-1, newColor)
            helper(image, src_color, r, c+1, newColor)
                    
                
        helper(image, image[sr][sc], sr, sc, newColor)
        return image