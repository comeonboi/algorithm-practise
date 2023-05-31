# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.num = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        result = []
        self.recur(root, 0, result)
        return len(result)
    def recur(self,node,level,result):
        if not node:
            return result
        result.append(node.val)
        self.recur(node.left, level+1, result)
        self.recur(node.right, level+1, result)
