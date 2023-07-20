class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result =[[]]
        self.back_tracking(nums,0,[],result)
        return result
    def back_tracking(self,nums,start_num,path,result):
        if sorted(path) not in result:
            result.append(sorted(path))
        for i in range(start_num,len(nums)):
            path.append(nums[i])
            self.back_tracking(nums, i+1, path, result)
            path.pop()