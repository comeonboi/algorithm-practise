class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 2. 用栈来做
        for i in nums:
            pass
        # 1. 暴力法
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] < nums[i]:
                    k -= 1
                    if k == 0:
                        return j - i + 1
        return 0
# Compare this snippet from leetcode\2383.赢得比赛需要的最少训练市场.py:
# from typing import List
