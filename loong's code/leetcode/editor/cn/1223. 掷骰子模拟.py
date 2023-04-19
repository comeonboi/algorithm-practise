from functools import cache
from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @cache
        def dfs(i: int, last: int, left: int) -> int:
            if i == 0:
                return 1
            res = 0
            for j, mx in enumerate(rollMax):
                if j != last:
                    res += dfs(i - 1, j, mx - 1)
                elif left:
                    res += dfs(i - 1, j, left - 1)
            return res % MOD

        return sum(dfs(n - 1, j, mx - 1) for j, mx in enumerate(rollMax)) % MOD


print(Solution.dieSimulator(Solution(), n=2, rollMax=[1, 1, 2, 2, 2, 3]))
