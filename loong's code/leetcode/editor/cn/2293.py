from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        flag = 0
        while len(nums) > 1:
            nums = [nums[i:i + 2] for i in range(0, len(nums), 2)]
            for i in range(len(nums)):
                if flag % 2 == 0:
                    nums[i] = min(nums[i])
                    flag += 1
                else:
                    nums[i] = max(nums[i])
                    flag += 1
        return nums[0]

print(Solution.minMaxGame(Solution(),nums = [1,3,5,2,4,8,2,2]))