# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = False
        l3 = ListNode()
        head = l3

        while l1 and l2:
            if flag:
                newVal = l1.val + l2.val + 1
            else:
                newVal = l1.val + l2.val

            if newVal < 10:
                l3.val = newVal
                flag = False
            else:
                l3.val = newVal - 10
                flag = True

            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                l3.next = ListNode()
                l3 = l3.next

        while l1:
            l3.next = ListNode()
            l3 = l3.next
            if flag:
                newVal = l1.val + 1
            else:
                newVal = l1.val
            if newVal < 10:
                l3.val = newVal
                flag = False
            else:
                l3.val = newVal - 10
                flag = True
            l1 = l1.next

        while l2:
            l3.next = ListNode()
            l3 = l3.next
            if flag:
                newVal = l2.val + 1
            else:
                newVal = l2.val
            if newVal < 10:
                l3.val = newVal
                flag = False
            else:
                l3.val = newVal - 10
                flag = True
            l2 = l2.next

        if flag:
            l3.next = ListNode()
            l3 = l3.next
            l3.val = 1

        return head
