from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        def dff(num1, num2):
            return num1 - num2
        start = 0
        tail_1 = 1
        tail_2 = 2
        count = 0
        while start < len(nums) and tail_1 < len(nums) and tail_2 < len(nums):
            dff_1 = nums[tail_1] - nums[start]
            dff_2 = nums[tail_2] - nums[tail_1]
            while dff_1 < diff:
                tail_1 += 1
                try :
                    dff_1 = nums[tail_1] - nums[start]
                except:
                    tail_2 -= 1
                    break
            while dff_2 < diff:
                tail_2 += 1
                try:
                    dff_2 = nums[tail_2] - nums[tail_1]
                except:
                    tail_2 -= 1
                    break
            if dff_1 == diff and dff_2 == diff:
                print(nums[start], nums[tail_1], nums[tail_2])
                count += 1
            start += 1
            tail_1 = start + 1
            tail_2 = start + 2
        return count
print(Solution().arithmeticTriplets(nums = [0,3,6,9], diff = 3))