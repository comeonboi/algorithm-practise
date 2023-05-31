# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = []
        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                self.ans.append(path + root.val)
                return
            dfs(root.left, path + root.val)
            dfs(root.right, path + root.val)
        dfs(root, 0)
        return targetSum in self.ans