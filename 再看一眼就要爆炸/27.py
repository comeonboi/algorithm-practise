class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return print(len(nums), ', nums =', set(nums))
        else:
            if val == nums[-1]:
                nums.pop()
                return self.removeElement(nums, val)
            else:
                x = nums[-1]
                nums.pop()
                nums.insert(0, x)
                return self.removeElement(nums, val)
