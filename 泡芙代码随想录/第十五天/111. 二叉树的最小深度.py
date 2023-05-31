# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = []
        deppth = []
        self.recur(root, 0, result, deppth)
        if not deppth:
            return 0
        return min(deppth)

    def recur(self, node, level, result, deppth):
        if not node:
            return result
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        self.recur(node.left, level + 1, result, deppth)
        self.recur(node.right, level + 1, result, deppth)
        if node.left == None and node.right == None:
            deppth.append(level + 1)
