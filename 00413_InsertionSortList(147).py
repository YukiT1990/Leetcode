# 147. Insertion Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is empty or only have 1 element, return head
        if not head:
            return None
        if not head.next:
            return head

        # Need four pointers and we are going to sort right at the same place
        # define dummy to hold the begining of the sorted list,
        # define temp to hold a value if order need to be changed
        # define current to loop over the list to be sorted
        # define runner to loop over the sorted linklist from dummy ->-> current

        dummy = ListNode(None, head)
        current = head

        while current.next is not None:
            # if in-order, move to the next number
            if current.next.val >= current.val:
                current = current.next

            # if current.next.val < current.val, list is not in-order,
            # we need to remove the current number from the origional linklist,
            # then do insertion from dummy.next
            else:
                temp = current.next
                runner = dummy
                current.next = current.next.next

                # insert the value in the sorted linklist
                while runner.next.val <= temp.val:
                    runner = runner.next
                runner.next, temp.next = temp, runner.next

        return dummy.next
