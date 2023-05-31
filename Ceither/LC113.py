# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        def dfs(root, path):
            if not root:
                 return
            path.append(root.val)
            if not root.left and not root.right and sum(path) == targetSum:
                self.ans.append(path[:])
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()
        dfs(root, [])
        return self.ans