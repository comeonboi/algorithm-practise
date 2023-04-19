from typing import List
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans_set = set()
        for i in range(1, n+1):
            if i not in banned:
                if sum(ans_set)+i <= maxSum:
                    ans_set.add(i)
                else:
                    break
        return len(ans_set)

print(Solution.maxCount(Solution() ,banned = [11], n = 7, maxSum = 50))