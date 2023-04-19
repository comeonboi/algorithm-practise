from collections import Counter
from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        pass
        # nums_source.sort()
        # max_count = 0
        #
        # # 当新数组与旧数组相同时，停止循环
        # for _ in range(len(nums)):
        #     nums_source = nums_source[1:] + [nums_source[0]]
        #     print(nums_source, nums)
        #     count = 0
        #     for i in range(len(nums)):
        #         if nums_source[i] > nums[i]:
        #             count += 1
        #             print(count)
        #     max_count = max(max_count, count)

        # nums.sort()
        # print(nums)
        # left = len(nums) - 1
        # dicts = Counter(nums)
        # count = 0
        # right = left
        # while right >= left >= 0:
        #     if nums[right] <= nums[left]:
        #         left -= 1
        #     if nums[right] > nums[left]:
        #         if dicts[nums[left]] > 0:
        #             dicts[nums[left]] -= 1
        #             left -= 1
        #             right -= 1
        #             count += 1
        #             #print(dicts, nums, count)
        #         else:
        #             left -= 1
        #     elif right == 0 or left == 0:
        #         break
        #
        # return count
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for x in nums:
            if x > nums[i]:
                i += 1
        return i



print(Solution.maximizeGreatness(Solution(), [1,3,5,2,1,3,1]))
