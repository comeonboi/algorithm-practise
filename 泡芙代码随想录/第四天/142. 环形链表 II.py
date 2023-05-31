# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        now = head
        res = -1
        while(now != None):
            if now not in node_list:
                node_list.append(now)
                now = now.next
                res+=1
            else:
                return now
        return None
