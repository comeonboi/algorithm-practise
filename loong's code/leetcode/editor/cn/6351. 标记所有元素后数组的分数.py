from math import inf
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        grade = 0
        bool_nums = [False] * len(nums)
        n = len(nums)
        seq = [(x, i) for i, x in enumerate(nums)]
        seq.sort()
        for x, i in seq:
            if bool_nums[i]:
                continue
            if i > 0:
                bool_nums[i - 1] = 1
            if i < n - 1:
                bool_nums[i + 1] = 1
            grade += x
        return grade

        # while set(nums) != {inf}:
        #     print(nums)
        #     mm = min(nums)
        #     min_index = nums.index(mm)
        #     grade += mm
        #     nums[min_index] = inf
        #     if min_index > 0:
        #         nums[min_index - 1] = inf
        #     if min_index < len(nums) - 1:
        #         nums[min_index + 1] = inf
        # return grade


print(Solution().findScore([4, 4, 4, 4]))
