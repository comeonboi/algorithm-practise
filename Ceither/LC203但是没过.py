class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        h1 = head
        if h1 == None:
            return h1
        while h1:
            if h1.val == val:
                h1 = h1.next
            else:
                break
            self.removeElements(h1, val)
        return h1