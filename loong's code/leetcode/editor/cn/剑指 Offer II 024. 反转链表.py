from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, pre = head, None

        def dfs(node, pre):
            if not node:
                return pre
            res = dfs(node.next, node)
            node.next = pre
            return res

        head = dfs(node, pre)
        return head


def list_to_linked_list(lst):
    if not lst:
        return None

    # 头结点
    head = ListNode(lst[0])
    current = head

    # 遍历列表中的元素，将其转换为链表节点
    for i in range(1, len(lst)):
        current.next = ListNode(lst[i])
        current = current.next

    return head


head = [1, 2, 3, 4, 5]
head = list_to_linked_list(head)
print(Solution.reverseList(Solution(), head))
current = head
while current:
    print(current.val)
    current = current.next
