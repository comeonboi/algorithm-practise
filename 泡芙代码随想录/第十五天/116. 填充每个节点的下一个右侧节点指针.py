"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        root_result = []
        self.recur(root, 0, root_result)
        for i in range(len(root_result)):
            for j in range(len(root_result[i])):
                if j != (len(root_result[i]) - 1):
                    root_result[i][j].next = root_result[i][j + 1]

        return root

    def recur(self, node, level, result):
        if not node:
            return result
        if len(result) == level:
            result.append([])
        result[level].append(node)
        self.recur(node.left, level + 1, result)
        self.recur(node.right, level + 1, result)
