class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        if len(nums) == 1:
            return 1 if nums[0]!=val else 0
        i = 0
        j = len(nums)-1
        while(i<j):
            if nums[i] == val:
                while(nums[j] == val and i < j):
                    j-=1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i+=1
            else:
                i+=1
        return j if nums[j] == val else j+1