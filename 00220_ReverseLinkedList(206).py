# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        if (not first) or (not first.next):
            return first
        first.next, curr, prev = None, first.next, first
        
        while curr.next:
            curr.next, curr, prev = prev, curr.next, curr
        curr.next = prev
        return curr