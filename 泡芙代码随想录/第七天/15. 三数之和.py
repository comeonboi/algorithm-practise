class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <3:
            return []
        i = 0
        j = 1
        k = 2
        result = []
        while (i < len(nums)-2):
            while(j < len(nums)-1):
                while(k < len(nums)):
                    aaa = sorted([nums[i],nums[j], nums[k]])
                    if nums[i]+nums[j]+nums[k] == 0 and aaa not in result:
                        result.append(aaa)
                        k+=1
                    else:
                        k += 1
                j += 1
                k = j+1
            i+=1
            j = i + 1
            k = j +1
        return result