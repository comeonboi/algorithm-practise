class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = len(nums)//2
        if mid == 0 :
            if target == nums[0]:
                return 0
            else:
                return -1
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            return self.search(nums[:mid], target)
        if target > nums[mid]:
            x = self.search(nums[mid:], target)
            if x == -1:
                return -1
            else:
                return x + mid
        return -1