import random
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 1
        while i < len(nums)-1:
            if nums[i] == (nums[i - 1] + nums[i + 1]) // 2:
                random.shuffle(nums)
                i = 1
            else:
                i += 1
        else:
            return nums



print(Solution.rearrangeArray(Solution(), nums= [3,2,1]))
