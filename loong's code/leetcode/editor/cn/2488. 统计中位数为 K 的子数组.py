from collections import Counter
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        # i=pos 的时候 x 是 0，直接记到 cnt 中，这样下面不是大于 k 就是小于 k
        cnt, x = Counter({0: 1}), 0
        for i in range(pos - 1, -1, -1):  # 从 pos-1 开始累加 x
            x += 1 if nums[i] < k else -1
            cnt[x] += 1

        # i=pos 的时候 x 是 0，直接加到答案中，这样下面不是大于 k 就是小于 k
        ans, x = cnt[0] + cnt[-1], 0
        for i in range(pos + 1, len(nums)):  # 从 pos+1 开始累加 x
            x += 1 if nums[i] > k else -1
            ans += cnt[x] + cnt[x - 1]
        return ans



print(Solution.countSubarrays(Solution(), nums=[3, 2, 1, 3, 5], k=4))
