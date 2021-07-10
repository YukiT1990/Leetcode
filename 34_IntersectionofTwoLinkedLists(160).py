# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def get_len(node):
            l = 0
            while node is not None:
                node = node.next
                l += 1
            return l

        lenA = get_len(headA)
        lenB = get_len(headB)
        for i in range(lenA - lenB):
            headA = headA.next
        for i in range(lenB - lenA):
            headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
