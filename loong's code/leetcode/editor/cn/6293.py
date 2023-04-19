from collections import Counter
from itertools import count
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        start = 0
        tail = 0
        flag = 0
        if len(set(nums)) == 1:
            if k > len(nums) * (len(nums)-1) // 2:
                return 0
        while start < len(nums) - 1:
            x = Counter(nums[start:tail])
            if len(x) >= k:
                flag2 = 0
                for j in x:
                    if x[j] >= k:
                        flag2 += 1
                if flag2 >= k:
                    flag += 1
            else:
                for i in x:
                    if x[i] * (x[i] - 1) // 2 >= k:
                        flag += 1
            if tail != len(nums):
                tail += 1
            else:
                start += 1

        return flag

print(Solution.countGood(Solution, nums = [1,1,1,1,1], k = 10))
