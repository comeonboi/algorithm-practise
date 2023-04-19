from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sums = 0

        for i in nums:
            if i >= 10:
                sums2 = 0
                for j in str(i):
                    sums2 += int(j)
                sums += abs(i - sums2)

        return sums
