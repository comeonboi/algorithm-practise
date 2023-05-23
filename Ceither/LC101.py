# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sub(self, r1: TreeNode, r2: TreeNode) -> bool:
        if r1 == None and r2 == None:
            return True
        elif r1 == None or r2 == None:
            return False
        elif r1.val == r2.val:
            return self.sub(r1.right, r2.left) and self.sub(r1.left, r2.right)
        else:
            return False
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.sub(root, root)