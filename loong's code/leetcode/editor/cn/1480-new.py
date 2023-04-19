class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # Input数组的输入
        # len（数组），m=0，str = []
        # for i in range(len(数组))：
        #    m += i
        #    str存入m
        m = 0
        length = len(nums)
        str1 = [0 for _ in range(length)]
        for i in range(length):
            m += nums[i]
            str1[i] = m
        return str1
        for i in range(0, 4, 2):
            print(i)

        if len(nums) <= 1:
            return nums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


print(Solution.runningSum(Solution, nums=[3, 1, 2, 10, 1]))
