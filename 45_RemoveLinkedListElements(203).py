# 203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = head
        pre = None

        # remove the node whose value is val if the head.val is val
        while cur and cur.val == val:
            head = cur.next
            cur = head


        while cur:
            while cur and cur.val != val:
                pre = cur
                cur = cur.next

            if cur == None:
                return head

            # remove the node whose value is val
            pre.next = cur.next
            cur = pre.next

        return head
