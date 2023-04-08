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
swapPairs()