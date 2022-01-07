# 382. Linked List Random Node

# Reference
# https://leetcode.com/problems/linked-list-random-node/discuss/1215808/Put-values-to-standard-list-85-speed

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.data = []
        while head:
            self.data.append(head.val)
            head = head.next
        self.len_data1 = len(self.data) - 1

    def getRandom(self) -> int:
        return self.data[randint(0, self.len_data1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()