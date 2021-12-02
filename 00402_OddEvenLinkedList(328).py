# 328. Odd Even Linked List

# Reference
# https://leetcode.com/problems/odd-even-linked-list/discuss/1351496/Python-w-explanation-of-while-loop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initiate heads of two lists and values to traverse linked list
        # odds = []
        # evens = []
        odds = ListNode(0)
        evens = ListNode(0)
        # create 2 heads for linked lists
        o_head = odds
        e_head = evens
        # first value is always ODD! thus is_odd = True
        is_odd = True

        # while head is not null
        while head:
            if is_odd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next

            # change is_odd from True <-> False, switching each time
            is_odd = not is_odd
            # keep incrementing head
            head = head.next

        # clarify the last value of evens list should be NULL
        evens.next = None
        # clarify last value of odds should be head of evens
        odds.next = e_head.next

        # o_head = odds -> thus prints out whole list
        return o_head.next
