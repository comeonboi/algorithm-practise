from collections import defaultdict
from itertools import chain
from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        cnt = defaultdict()
        for i, j in chain(items1, items2):
            cnt[i] += j
        return sorted(cnt.items())


print(Solution.mergeSimilarItems(Solution(), items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]))
