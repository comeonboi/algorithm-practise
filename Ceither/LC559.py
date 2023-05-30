"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return max(self.maxDepth(node) for node in root.children) + 1 if root and root.children else int(root is not None)