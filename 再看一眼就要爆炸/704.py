import math
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = math.ceil(len(nums))
        if target == nums[mid]:
            return print(mid)
        if target < nums[mid]:
            return self.search(self, nums[:mid], target)
        elif target > nums[mid]:
            return self.search(self, nums[mid:], target)
        else:
            return print(-1)

