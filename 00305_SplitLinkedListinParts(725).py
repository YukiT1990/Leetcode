# 725. Split Linked List in Parts

# Reference
# https://leetcode.com/problems/split-linked-list-in-parts/discuss/469189/Python-3-(ten-lines)-(36-ms)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        A, B, i = [], [], 0
        while head != None: head, _ = head.next, A.append(head.val)
        LA = len(A)
        (n, r) = divmod(LA, k) if k < LA else (1, 0)
        A.extend([0]*(k - LA))
        for s in range(k):
            L = LH = ListNode(A[i])
            for j in range(i+1, i+n+(r>0)):
                L.next = ListNode(A[j])
                L = L.next 
            i, r, _ = i + n + (r>0), r - 1, B.append(LH if s<LA else None)
        return B