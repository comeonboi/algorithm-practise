class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        n1 = head
        nodes = []
        while n1:
            if n1 in nodes:
                return n1
            nodes.append(n1)
            n1 = n1.next
        return None