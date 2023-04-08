# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        n = 0
        start = head
        end = head
        now = head
        pre = None
        if head.next != None:
            res = head.next
        else:
            res = head
        while (now!= None):
            if (n==1):
                end = now
                now = now.next
                if pre != None:
                    pre.next = end
                self.reverse(start,end,now)
                pre = start
                start = now
                n=0
            else:
                now = now.next
                n+=1
        return res
    def reverse(self, start,end, follow):
        now = start
        pre = None
        while (now != follow and now != None):
            temp = now.next
            now.next = pre
            pre = now
            now = temp
        n = 0
        start.next = follow