"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        self.recur(root,0,result)
        return result
    def recur(self,node,level,result):
        if not node:
            return result
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        for i in range(len(node.children)):
            self.recur(node.children[i], level+1, result)