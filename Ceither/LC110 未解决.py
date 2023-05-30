# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)
        if abs(l - r) <= 1:
            return True