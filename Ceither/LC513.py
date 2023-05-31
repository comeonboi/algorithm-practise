# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_depth = None
        self.ans = None

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # 层序遍历
        # queue = [root]
        # while queue:
        #     node = queue.pop(0)
        #     if node.right:
        #         queue.append(node.right)
        #     if node.left:
        #         queue.append(node.left)
        # return node.val
        # 递归
        self.max_depth = 0
        self.ans = 0
        a = root
        if not a:
            return 0
        return self.dfs(a, 1)

    def dfs(self, root, depth):
        if not root:
            return
        if depth > self.max_depth:
            self.max_depth = depth
            self.ans = root.val
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
        return self.ans