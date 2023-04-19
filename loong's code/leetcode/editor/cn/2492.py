from cmath import inf
from typing import List
import numpy as np


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        matrix = np.full((n, n), -1)
        matrix1 = [False]*n
        for i in roads:
            matrix[i[0] - 1, i[1] - 1] = matrix[i[1] - 1, i[0] - 1] = i[2]
        ans = inf

        def dfs(x: int) -> None:
            nonlocal ans
            matrix1[x] = True
            flag = 0
            for j in matrix[x]:
                flag += 1
                if j > 0:
                    ans = min(ans, j)
                if not matrix1[flag-1]:
                    dfs(flag)

        dfs(0)
        return int(ans)


print(Solution.minScore(Solution(), n=4, roads=[[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))
