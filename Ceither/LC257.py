# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.dfs(root, [])
        return self.ans

    def dfs(self, root, path):
        if not root:
            return
        path.append(str(root.val))
        if not root.left and not root.right:
            self.ans.append('->'.join(path))
        self.dfs(root.left, path)
        self.dfs(root.right, path)
        path.pop()