class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        for i in range(len(nums)):
            if nums[length] != val:
                length += 1
            else:
                nums.remove(nums[length])
        return length
