from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next == None:
            return head
        p = head
        q = head.next
        p.next = self.swapPairs(q.next)
        q.next = p
        return q
