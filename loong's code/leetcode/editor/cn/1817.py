from collections import defaultdict
from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dict1 = defaultdict(set)
        list1 = [0] * k
        for i, j in logs:
            dict1[i].add(j)
        for i in dict1:
            print(dict1[i])
            # TypeError object of type ‘type‘ has no len() 是因为dict少打了1
            list1[len(dict1[i]) - 1] += 1
        return list1



print(Solution.findingUsersActiveMinutes(Solution, logs=[[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], k=5))
