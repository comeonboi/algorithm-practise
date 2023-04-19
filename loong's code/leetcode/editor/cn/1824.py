from collections import deque
from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dis = [[n] * 3 for _ in range(n)]
        dis[0][1] = 0
        q = deque([(0, 1)])  # 起点
        while True:
            i, j = q.popleft()
            d = dis[i][j]
            if i == n - 1: return d  # 到达终点
            if obstacles[i + 1] != j + 1 and d < dis[i + 1][j]:  # 向右
                dis[i + 1][j] = d
                q.appendleft((i + 1, j))  # 加到队首
            for k in (j + 1) % 3, (j + 2) % 3:  # 枚举另外两条跑道（向上/向下）
                if obstacles[i] != k + 1 and d + 1 < dis[i][k]:
                    dis[i][k] = d + 1
                    q.append((i, k))  # 加到队尾
