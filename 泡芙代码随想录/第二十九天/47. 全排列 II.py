class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.back_tracking(nums, [], result, len(nums),set())
        return result

    def back_tracking(self, nums, path, result, length,used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in used:
                continue
            if i not in used:
                used.add(i)
                path.append(nums[i])
                self.back_tracking(nums, path, result, length,used)
                path.pop()
                used.remove(i)
                