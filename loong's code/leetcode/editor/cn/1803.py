from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        flag = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # print("i:",i, "j:", j, " nums[i]:",nums[i],"nums[j]:",nums[j], nums[i]^nums[j])
                if low<=nums[i]^nums[j] <= high:
                    flag += 1
        return flag
print(Solution.countPairs(Solution(),nums = [1,4,2,7], low = 2, high = 6))