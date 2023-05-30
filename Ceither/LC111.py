# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        # return min(l, r) + 1 if l and r else l + r + 1
        return l + r + 1 if l == 0 or r == 0 else min(l, r) + 1