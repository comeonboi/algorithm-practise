class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        tempSum = nums[0]
        result = float('inf')
        while (j < len(nums) and i <len(nums)):
            if tempSum >= target:
                if (j-i+1) <= result:
                    result = (j-i+1)
                    tempSum -= nums[i]
                    i+=1
                else:
                    tempSum -= nums[i]
                    i+=1
            else:
                j+=1
                if (j<=(len(nums)-1)):
                    tempSum += nums[j]
        return result if result != float('inf') else 0
