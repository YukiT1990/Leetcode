# 876. Middle of the Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        start = head
        while start:
            values.append(start.val)
            start = start.next 
        middle = len(values) // 2
        # print(head)
        while middle > 0:
            head = head.next
            middle -= 1
        return head