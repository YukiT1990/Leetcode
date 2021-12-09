# 1306. Jump Game III

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        q.append(start)
        visited = set()
        
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            
            visited.add(i)
            
            left_neighbor_i, right_neighbor_i = i - arr[i], i + arr[i]
            if left_neighbor_i >= 0 and left_neighbor_i not in visited:
                q.append(left_neighbor_i)
            if right_neighbor_i < len(arr) and right_neighbor_i not in visited:
                q.append(right_neighbor_i)
        
        return False