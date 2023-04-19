from collections import Counter
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def res(num: int) -> int:
            return int(str(num)[::-1])
        cnt = Counter()
        ans = 0
        for i in nums:
            j = res(i)
            # 当cnt[i-res(i)]不存在时，会返回0.
            ans += cnt[i-j]
            # 因此在cnt[i-j] 有2次值的时候才会返回到ans中
            # 因为cnt[]=1时，是不会经过ans赋值的
            cnt[i-j] += 1
        return ans % (10 ** 9 + 7)


print(Solution.countNicePairs(Solution(), nums=[42, 11, 1, 97]))
