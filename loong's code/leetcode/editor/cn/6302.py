from typing import List

#这是一个动态规划问题。首先，我们需要定义状态，其中dp[i][j]表示从前i个元素中选择j个元素的最大分数。

# 我们可以使用以下状态转移方程来求解此问题：
#
# dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + (nums1[i-1] * min(nums2[i-1], nums2[i-2], ..., nums2[i-j]))
#
# 其中，在转移方程的第二项中，我们需要找到nums2中从i-1开始选择j个元素的最小值。我们可以使用一个滑动窗口来维护这个值。
#
# 最终，我们可以使用dp[n][k]来获得最大分数。
#
# 请注意，此算法的时间复杂度为O(nk)，空间复杂度为O(nk)，可能会超出限制。您可以考虑优化空间复杂度。
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        min_nums2 = [0] * (n + 1)
        for i in range(1, n + 1):
            min_nums2[i] = min(min_nums2[i - 1], nums2[i - 1])
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + (nums1[i - 1] * min_nums2[i - j + 1]))
        return dp[n][k]


print(Solution.maxScore(Solution(), nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3))
