# 690. Employee Importance

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # 227 ms	15.6 MB
        importance_sum = 0
        def helper(e_id: int):
            nonlocal importance_sum
            for emp in employees:
                if emp.id == e_id:
                    importance_sum += emp.importance
                    if len(emp.subordinates) > 0:
                        for sub in emp.subordinates:
                            helper(sub)
                    break
        helper(id)
        return importance_sum
    
        # 156 ms	15.7 MB
        # Reference
        # https://leetcode.com/problems/employee-importance/discuss/332600/Iterative-Python-beats-99.73
        # id_to_emp = {employee.id: employee for employee in employees}
        # importance = 0
        # stack = [id_to_emp[id]]
        # while stack:
        #     cur_emp = stack.pop()
        #     importance += cur_emp.importance
        #     stack.extend([id_to_emp[new_emp] for new_emp in cur_emp.subordinates])
        # return importance 