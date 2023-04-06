class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        mid = int((i+j)/2)
        while(i<j):
            if(nums[mid] == target):
                break
            elif(nums[mid] > target):
                j = mid-1
                mid = int((i+j)/2)
            else:
                i = mid+1
                mid = int((i+j)/2)
        if nums[mid] == target:
            return mid
        else:
            return -1