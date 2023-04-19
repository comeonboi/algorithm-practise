from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursion(nums, left, right, target):
            if left > right:
                # 递归结束
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            return recursion(nums, left, right, target)

        left = 0
        right = len(nums) - 1
        return recursion(nums, left, right, target)


print(Solution.search(Solution(), nums=[-1, 0, 3, 5, 9, 12], target=9))
