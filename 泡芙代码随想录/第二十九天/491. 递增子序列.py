class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.back_tracking(nums, 0, [], result)
        return result

    def back_tracking(self, nums, start_index, path, result):
        if len(path) >= 2:
            result.append(path[:])
        used = set()
        for i in range(start_index, len(nums)):
            if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                used.add(nums[i])
                path.append(nums[i])
                self.back_tracking(nums, i + 1, path, result)
                path.pop()
