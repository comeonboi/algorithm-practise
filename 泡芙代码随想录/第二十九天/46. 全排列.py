class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.back_tracking(nums, [], result, len(nums))
        return result

    def back_tracking(self, nums, path, result, length):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(length):
            if nums[i] not in path:
                path.append(nums[i])
                self.back_tracking(nums, path, result, length)
                path.pop()