# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.recur(root,0,result)
        re = []
        for i in range(len(result)):
            re.append(result[i][-1])
        return re

    def recur(self,root,level,result):
        if not root:
            return result
        if len(result)==level:
            result.append([])
        result[level].append(root.val)
        self.recur(root.left, level+1, result)
        self.recur(root.right, level+1, result)