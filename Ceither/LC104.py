# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        l = root
        r = root
        if root is None:
            return 0
        return max(self.maxDepth(l.left), self.maxDepth(r.right)) + 1