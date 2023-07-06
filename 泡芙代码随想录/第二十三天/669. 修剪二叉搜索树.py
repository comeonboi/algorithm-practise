# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        return self.recur(root, low, high)

    def recur(self, root, low, high):
        if not root:
            return None
        if root.val < low:
            return self.recur(root.right, low, high)
        if root.val > high:
            return self.recur(root.left, low, high)
        root.left = self.recur(root.left, low, high)
        root.right = self.recur(root.right, low, high)
        return root


