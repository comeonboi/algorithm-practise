from typing import List
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        m = 0
        for ind, i in enumerate(nums):
            right = ind + 1
            if right >= len(nums):
                break
            flag = 1
            while right < len(nums) and nums[right] - nums[right-1] == flag:
                right += 1
                flag *= -1
            # print(nums[right] - nums[ind])
            m = max(m, right - ind)
        return m if m > 0 else -1

print(Solution().alternatingSubarray(nums = [21,9,5]))