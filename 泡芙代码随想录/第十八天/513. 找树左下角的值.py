# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result = []
        self.recur(root,0,result)
        return result[-1][0]
    def recur(self,node,level,result):
        if not node:
            return []
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        if node.left:
            self.recur(node.left,level+1,result)
        if node.right:
            self.recur(node.right,level+1,result)