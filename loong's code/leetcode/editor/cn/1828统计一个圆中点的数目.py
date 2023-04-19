from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 求解点到圆心的欧式距离是否小于 r
        ans = [0] * len(queries)
        flag = 0
        for x, y, r in queries:
            for i, j in points:
                if ((x - i) ** 2 + (y - j) ** 2) ** (1 / 2) <= r:
                    ans[flag] += 1
            flag += 1
        return ans


print(Solution.countPoints(Solution(), points=[[1, 3], [3, 3], [5, 3], [2, 2]],
                           queries=[[2, 3, 1], [4, 3, 1], [1, 1, 2]]))
