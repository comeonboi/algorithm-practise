# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        now = head
        pre = None
        while(now != None):
            nextt = now.next
            now.next = pre
            pre = now
            now = nextt
        return pre