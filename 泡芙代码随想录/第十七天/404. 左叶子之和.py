# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = []
        self.recur(root, 0, result)
        return sum(result)

    def recur(self, node, level, result):
        if not node:
            return []
        if node.left:
            if not node.left.left and not node.left.right:
                result.append(node.left.val)
            self.recur(node.left, level + 1, result)
        if node.right:
            self.recur(node.right, level + 1, result)
