class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hash_table = {}
        h1 = headA
        h2 = headB
        while h1:
            hash_table[h1] = 1
            h1 = h1.next
        while h2:
            if h2 in hash_table:
                return h2
            h2 = h2.next
        return None