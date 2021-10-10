# 1290. Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next 
        nums = list(map(str, nums))
        nums = ''.join(nums)
        return int(nums, 2)