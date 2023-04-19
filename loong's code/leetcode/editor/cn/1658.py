from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        ans = -1
        left = s = 0
        for right, x in enumerate(nums):
            s += x
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        return -1 if ans < 0 else len(nums) - ans

print(Solution.minOperations(Solution(), nums = [1,1,4,2,3], x = 5))