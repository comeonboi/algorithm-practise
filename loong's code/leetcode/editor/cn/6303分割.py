from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            for j in str(i):
                ans.append(int(j))
        return ans


print(Solution.separateDigits(Solution, nums=[13, 25, 83, 77,1]))
