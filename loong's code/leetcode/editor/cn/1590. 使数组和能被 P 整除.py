from itertools import accumulate
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = list(accumulate(nums, initial=0))
        x = s[-1] % p
        if x == 0:
            return 0
        ans = n = len(nums)
        last = {}
        for i, v in enumerate(s):
            last[v % p] = i
            j = last.get((v - x) % p, -n)
            ans = min(ans, i - j)
        return ans if ans < n else -1
