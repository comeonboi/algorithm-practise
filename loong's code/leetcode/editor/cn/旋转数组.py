import copy
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums = nums[k:] + nums[:len(nums) - k + 1]
        print(nums)


print(Solution.rotate(Solution(), nums=[-1, -100, 3, 99], k=2))


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums1 = [None] * len(nums)
        for i in range(len(nums)):
            nums1[(i + k) % len(nums)] = nums[i]
        nums.clear()
        for i in nums1:
            nums.append(i)
        print(nums)


print(Solution.rotate(Solution(), nums=[1, 2, 3, 4, 5, 6, 7], k=3))
