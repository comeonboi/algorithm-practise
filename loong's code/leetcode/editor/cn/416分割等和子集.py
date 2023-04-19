from typing import List

# cuo de
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        index = 1 // 2 * len(nums)
        set1 = set()
        while index > 0 or index < len(nums):
            if sum(nums[:index]) == sum(nums[index:]):
                return True
            elif sum(nums[:index]) < sum(nums[index:]):
                index += 1
                if index in set1:
                    return False
                else:
                    set1.add(index)
            else:
                index -= 1
                if index in set1:
                    return False
                else:
                    set1.add(index)
        return False


print(Solution.canPartition(Solution(), nums=[1, 5, 11, 5]))
