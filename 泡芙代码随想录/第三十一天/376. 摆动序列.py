class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return len(nums)
        curDiff = 0
        preDiff = 0
        result = 1
        for i in range(len(nums)-1):
            curDiff = nums[i + 1] - nums[i]
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1  # 峰值个数加1
                preDiff = curDiff  # 注意这里，只在摆动变化的时候更新preDiff
        return result  # 返回最长摆动子序列的长度