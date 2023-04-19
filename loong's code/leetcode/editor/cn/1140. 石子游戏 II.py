from functools import cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        M = 1
        n = len(piles)
        for i in range(n - 2, -1, -1):
            piles[i] += piles[i + 1]  # 后缀和

        @cache
        def dfs(i: int, m: int) -> int:
            if i + m * 2 >= n:  # 能全拿
                return piles[i]
            return piles[i] - min(dfs(i + x, max(m, x)) for x in range(1, m * 2 + 1))
        return dfs(0, 1)
