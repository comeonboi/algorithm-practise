from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursion(nums, left, right, target):
            if left > right:
                return -1
            mid = left + (left - right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            return recursion(nums, left, right, target)