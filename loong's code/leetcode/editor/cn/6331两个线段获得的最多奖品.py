from typing import List
from collections import defaultdict, Counter


class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        # 计算前缀和
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + prizePositions[i - 1]

        # dp数组
        dp = [0] * (n - 2 * k + 2)
        left = [0] * (n - 2 * k + 2)
        right = [0] * (n - 2 * k + 2)

        # 更新dp数组
        for i in range(n - 2 * k + 1):
            if presum[i + k] - presum[i] > dp[i - 1]:
                dp[i] = presum[i + k] - presum[i]
                left[i] = i
            else:
                dp[i] = dp[i - 1]
                left[i] = left[i - 1]

        # 更新right数组
        for i in range(n - 2 * k, -1, -1):
            if presum[i + 2 * k] - presum[i + k] >= dp[i + 1]:
                dp[i] = presum[i + 2 * k] - presum[i + k] + dp[left[i]]
                right[i] = i + k
            else:
                dp[i] = dp[i + 1] + dp[left[i]]
                right[i] = right[i + 1]

        # 最终的结果
        res = [0] * 3
        for i in range(k, n - 2 * k + 1):
            if dp[i - k] > dp[res[0]]:
                res = [i - k, i, right[i - k]]
        return res

print(Solution.maximizeWin(Solution(), prizePositions=[1, 1, 2, 2, 3, 3, 5], k=2))
