class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        maxNum = 0
        nums = sorted(list(set(nums)))
        if nums:
            flag = 1
        else:
            flag = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                flag += 1
            else:
                maxNum = max(maxNum, flag)
                flag = 1
        else:
            maxNum = max(maxNum, flag)
        return maxNum


print(Solution.longestConsecutive
      (Solution, nums=[100,4,200,1,3,2])
      )
