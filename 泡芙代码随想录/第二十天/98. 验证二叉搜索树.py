# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = self.check(root)
        for i in range(1, len(result)):
            if result[i] <= result[i - 1]:
                return False
        return True

    def check(self, root):
        if not root:
            return []
        left = self.check(root.left)
        right = self.check(root.right)
        return left + [root.val] + right
