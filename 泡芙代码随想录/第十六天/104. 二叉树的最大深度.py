# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = []
        self.recur(root,0,result)
        return len(result)
    def recur(self,node,levle,result):
        if not node:
            return result
        if len(result) == levle:
            result.append([])
        result[levle].append(node.val)
        self.recur(node.left, levle+1, result)
        self.recur(node.right, levle+1, result)