# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head != None:
            current = head
            current_next = current.next
            while current_next:
                if current.val == current_next.val:
                    current.next = current_next.next
                    current_next = current_next.next
                else:
                    current = current_next
                    current_next = current_next.next
            return head
        return None
