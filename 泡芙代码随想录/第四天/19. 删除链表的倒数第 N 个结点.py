# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        faster = head
        slow = head
        pre = None
        while (n > 1):
            faster = faster.next
            n -= 1
        while(faster.next != None):
            faster = faster.next
            pre = slow
            slow = slow.next
        if pre == None:
            return slow.next
        else:
            pre.next = slow.next
        return head