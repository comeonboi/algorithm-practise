# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        i = 0
        j = 0
        nowA = headA
        nowB = headB
        while nowA != None:
            nowA = nowA.next
            i+=1
        while nowB != None:
            nowB = nowB.next
            j+=1
        if i>j:
            n = i-j
            while n > 0:
                headA = headA.next
                n-=1
        elif j>i:
            n = j-i
            while n > 0:
                headB = headB.next
                n-=1
        while (headA != headB and headA!= None and headB != None):
            headA = headA.next
            headB = headB.next
        return headA
