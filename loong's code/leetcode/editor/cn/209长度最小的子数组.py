from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1  # inf
        s = 0
        left = 0
        for right, x in enumerate(nums):
            # 记录前一次的相加结果
            s += x
            # 移动左端点,left <= right,因为这个数前面的和s已经>=target了，所以从前面的s中减少数字判断是否还能减少
            # while s - nums[left] >= target:
            #     s -= nums[left]
            #     left += 1
            # if s >= target:
            #     ans = min(ans, right - left + 1)

            while s >= target:  # 满足要求
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1

        return ans if ans <= n else 0


print(Solution.minSubArrayLen(Solution(), target=7, nums=[2, 3, 1, 2, 4, 3]))
