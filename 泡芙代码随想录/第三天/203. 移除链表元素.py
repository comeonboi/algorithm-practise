# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        delete_node = None
        fetch_node = None
        result = head
        while (result != None):
            if result.val == val:
                result = result.next
            else:
                break
        now = result
        while(now != None):
            if now.next == None:
                break
            if now.next.val == val:
                now.next = now.next.next
            else:
                now = now.next
        return result