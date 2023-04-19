from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = [0, len(nums)]
        for index in range(1, len(nums)):
            if nums[index - 1] == nums[index]:
                ans[0] += 1
                ans[1] -= 2
                nums[index - 1] = nums[index] = -1
        return ans


print(Solution.numberOfPairs(Solution(), nums=[1, 3, 2, 1, 3, 2, 2]))
