import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        diff = lambda x, y: (x + 1) / (y + 1) - x / y

        q = list()
        ans = 0.
        for x, y in classes:
            ans += x / y
            # python 中的优先队列是小根堆，所以要对增加量取相反数，达到大根堆的效果
            q.append((-diff(x, y), x, y))

        heapq.heapify(q)

        for _ in range(extraStudents):
            d, x, y = heapq.heappop(q)
            ans += -d
            heapq.heappush(q, (-diff(x + 1, y + 1), x + 1, y + 1))

        return ans / len(classes)
