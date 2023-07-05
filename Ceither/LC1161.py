class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []

        def dfs(root, level):
            if not root:
                return
            if level == len(sums):
                sums.append(root.val)
            else:
                sums[level] += root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        return sums.index(max(sums)) + 1