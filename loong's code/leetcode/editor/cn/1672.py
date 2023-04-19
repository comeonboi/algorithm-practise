from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = -1
        for i in accounts:
            sums = 0
            sums += sum(i)
            max_sum = max(sums, max_sum)
        return max_sum


print(Solution.maximumWealth(Solution(), accounts=[[1, 2, 3], [3, 2, 1]]))
