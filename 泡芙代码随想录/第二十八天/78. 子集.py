class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        self.back_tracking(nums, [], result, 0)
        return result

    def back_tracking(self, nums, path, result, start):
        if path not in result:
            result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.back_tracking(nums, path, result, i + 1)
            path.pop()
