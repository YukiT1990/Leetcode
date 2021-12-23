# 210. Course Schedule II

# Reference
# https://leetcode.com/problems/course-schedule-ii/discuss/1327646/Elegant-Python-DFS

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Handle edge case.
        if not prerequisites: return [course for course in range(numCourses)]
        
        # 'parents' maps each course to a list of its pre
		# -requisites.
        parents = {course: [] for course in range(numCourses)}
        for course, prerequisite in prerequisites:
            parents[course].append(prerequisite)
            
        topological_order = []
        visited, current_path = [False]*numCourses, [False]*numCourses
        
        # Returns False if the digraph rooted at 'course'
		# is acyclic, else, appends courses to 'topological
        # _order' in topological order and returns True.
        def dfs(course):
            if current_path[course]: return False
            if visited[course]: return True
            visited[course], current_path[course] = True, True
            if parents[course]:
                for parent in parents[course]:
                    if not dfs(parent): return False
            topological_order.append(course)
            current_path[course] = False
            return True
        
        for course in range(numCourses):
            if not dfs(course): return []
            
        return topological_order
        