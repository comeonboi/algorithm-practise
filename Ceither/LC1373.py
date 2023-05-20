class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> tuple:
            if not root:
                return 1, inf, -inf, 0
            l, lmin, lmax, lsum = dfs(root.left)
            r, rmin, rmax, rsum = dfs(root.right)
            if l and r and lmax < root.val < rmin:
                nonlocal ans
                s = lsum + rsum + root.val
                ans = max(ans, s)
                return 1, min(lmin, root.val), max(rmax, root.val), s
            return 0, 0, 0, 0

        ans = 0
        dfs(root)
        return ans