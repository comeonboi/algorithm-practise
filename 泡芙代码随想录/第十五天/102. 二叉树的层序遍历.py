# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.recur(root,0,result)
        return result
    def recur(self, node, level, result):
        if not node:
            return result
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        self.recur(node.left, level+1, result)
        self.recur(node.right, level+1, result)