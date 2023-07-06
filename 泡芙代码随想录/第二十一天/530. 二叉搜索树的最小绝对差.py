# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = self.getInorderList(root)
        minDifference = float('inf')
        for i in range(1, len(result)):
            for j in range(i):
                if result[i] - result[j] < minDifference:
                    minDifference = result[i] - result[j]
        return minDifference

    def getInorderList(self, root):
        if not root:
            return []
        result = []
        left = self.getInorderList(root.left)
        right = self.getInorderList(root.right)
        return left + [root.val] + right