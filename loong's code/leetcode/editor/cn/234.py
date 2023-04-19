# Definition for singly-linked list.
from typing import *


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#     def setValue(self, new_value):
#         self.val = new_value
#
#     def setNext(self, new_next):
#         self.next = new_next
#
#     def getNext(self):
#         return self.next
#
#
# class LinkedList(object):
#     def __init__(self):
#         self.head = ListNode()
#         self.tail = None
#         self.length = 0
#
#     def isEmpty(self):
#         return self.head is None
#
#     def add(self, value):
#         newnode = ListNode(value, None)
#         newnode.setNext(self.head)
#         self.head = newnode
#
#     def append(self, value):
#         newnode = ListNode(value)
#         if self.isEmpty():
#             self.head = newnode
#         else:
#             current = self.head
#             while current.getNext() is not None:
#                 current = current.getNext()
#             current.setNext(newnode)


class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast, prev = head, head, None

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        return True


head = ListNode()
head = input()

# a = ListNode
# for i in range(0, len(list1)):
#     a = ListNode(int(list1[i]))
test = Solution()
ListNode(1,2,2,1)
test.isPalindrome([1,2,2,1])
