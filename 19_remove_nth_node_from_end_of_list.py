# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=slow=dummy=ListNode(0,head)

        for i in range(n+1):
            fast=fast.next
        while (fast):
            slow=slow.next
            fast=fast.next
        slow.next = slow.next.next
        return dummy.next
        