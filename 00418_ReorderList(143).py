# 143. Reorder List

# Reference
# https://leetcode.com/problems/reorder-list/discuss/1640529/Python3-ONE-PASS-L(o)-Explained

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return

        # search for the middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        tail, cur = None, slow.next
        slow.next = None  # detach list on the middle

        # reverse right part
        while cur:
            cur.next, tail, cur = tail, cur, cur.next

            # rearrange nodes as asked
        headCur, headNext = head, head.next
        tailCur, tailNext = tail, tail.next
        while True:
            headCur.next, tailCur.next = tailCur, headNext

            if not tailNext:
                return

            tailCur, headCur = tailNext, headNext
            tailNext, headNext = tailNext.next, headNext.next
